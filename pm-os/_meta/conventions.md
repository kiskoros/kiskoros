# Convenciones del vault

## Frontmatter

```yaml
---
type: daily | weekly | project | decision | case-study | meeting | interview | literature | prd | moc | note
status: seed | growing | evergreen   # madurez de la idea
created: 2026-01-31
tags: []
publish: false        # true solo si es público
confidential: false   # true bloquea publish.py aunque publish sea true
---
```

## Estados de madurez

- `seed`: captura o idea breve.
- `growing`: se está desarrollando.
- `evergreen`: estable, vale como referencia.

Coincide con la progresión de `trastienda/` (`seed`, `growing`, `published`).

## Nombres de archivo

- Notas con título: `kebab-case.md` (`prioridad-con-rice.md`).
- Diario: `AAAA-MM-DD.md`. Semanal: `AAAA-Wnn.md`.
- Decisiones: `AAAA-MM-DD-titulo-corto.md`.

## Enlaces y tags

- Enlaza con `[[wikilinks]]`; la relación entre notas vale más que el tag.
- Tags solo para filtrar por dimensión transversal: `#producto/discovery`, `#producto/estrategia`, `#carrera`.
- Cada proyecto y cada decisión enlazan a la nota de la que nacen.

## Qué se puede publicar

Antes de poner `publish: true`, comprueba:

- [ ] No aparece cliente, empresa ni persona identificable sin permiso.
- [ ] No hay cifras internas; los porcentajes se expresan de forma relativa o aproximada.
- [ ] Las citas de entrevistas están pseudonimizadas.
- [ ] Tengo permiso de mi empleador o cliente, si aplica.
- [ ] Las notas a las que enlaza también se publican, o el enlace sobra.
