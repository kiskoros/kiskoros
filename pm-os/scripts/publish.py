#!/usr/bin/env python3
"""Copia al destino las notas del vault marcadas con `publish: true`.

Uso:
    python3 scripts/publish.py DESTINO            # simulación (por defecto)
    python3 scripts/publish.py DESTINO --apply    # copia de verdad

Reglas de seguridad:
  * Solo se publica lo que dice `publish: true` en el frontmatter.
  * Si la nota dice además `confidential: true`, el script aborta.
  * Avisa de enlaces [[...]] hacia notas que no se publican.
  * Nunca toca _templates/, _meta/, scripts/ ni .obsidian/.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"_templates", "_meta", "scripts", ".obsidian", ".git", "_local"}
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def frontmatter(text):
    match = FRONTMATTER.match(text)
    data = {}
    if not match:
        return data
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "-")):
            key, _, value = line.partition(":")
            data[key.strip()] = value.split("#")[0].strip().lower()
    return data


def notes():
    for path in sorted(VAULT.rglob("*.md")):
        rel = path.relative_to(VAULT)
        if rel.parts[0] in SKIP_DIRS or any(p.startswith(".") for p in rel.parts):
            continue
        yield path, rel


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("destino", type=Path)
    parser.add_argument("--apply", action="store_true", help="copiar de verdad")
    args = parser.parse_args()

    published, all_stems = {}, set()
    for path, rel in notes():
        all_stems.add(path.stem)
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("publish") == "true":
            if meta.get("confidential") == "true":
                sys.exit(f"ABORTADO: {rel} tiene publish: true y confidential: true")
            published[rel] = text

    if not published:
        print("No hay notas con publish: true. Nada que hacer.")
        return

    published_stems = {rel.stem for rel in published}
    warnings = []
    for rel, text in published.items():
        for target in {m.strip() for m in WIKILINK.findall(text)}:
            if target in all_stems and target not in published_stems:
                warnings.append(f"{rel} enlaza a [[{target}]], que NO se publica")

    mode = "COPIANDO" if args.apply else "SIMULACIÓN (usa --apply para copiar)"
    print(f"{mode} → {args.destino}")
    for rel in published:
        print(f"  {rel}")
        if args.apply:
            target = args.destino / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(VAULT / rel, target)

    for warning in warnings:
        print(f"AVISO: {warning}")
    print(f"{len(published)} nota(s), {len(warnings)} aviso(s).")


if __name__ == "__main__":
    main()
