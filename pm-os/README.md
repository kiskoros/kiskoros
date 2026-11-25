# PM Operating System · Second Brain

Un vault de Obsidian, versionado con Git, que sirve a tres cosas a la vez:

1. **Operar**: el día a día de producto (foco, reuniones, proyectos, decisiones).
2. **Pensar**: un segundo cerebro (lecturas, ideas, frameworks) que se acumula con el tiempo.
3. **Mostrar**: un portfolio construido a partir de lo que ya escribes, sin trabajo extra.

## Modelo de privacidad (léelo primero)

Git no olvida. Todo lo que se sube a un repo público queda en su historial aunque lo borres después.

| Capa | Dónde vive | Qué contiene |
| --- | --- | --- |
| **Vault completo** | Repo **privado** (recomendado: `second-brain`) | Todo tu historial: diario, reuniones, entrevistas, decisiones, borradores |
| **Portfolio** | Este repo público (`kiskoros/kiskoros`) | Solo notas con `publish: true`, copiadas con `scripts/publish.py` |

Así conservas **todo** tu historial versionado, y lo público es una selección deliberada.

Regla simple: *si dudas, no lleva `publish: true`*. El script además se niega a publicar notas con `confidential: true`.

## Estructura

```
00-inbox/       captura rápida, sin orden (se vacía cada semana)
01-projects/    iniciativas con objetivo y fin (un producto, una discovery, un lanzamiento)
02-areas/       responsabilidades continuas (estrategia, stakeholders, carrera, métricas)
03-resources/   conocimiento reutilizable (frameworks, lecturas, plantillas)
04-archive/     lo terminado o inactivo
05-journal/     daily/ y weekly/
06-decisions/   registro de decisiones (una nota por decisión)
07-portfolio/   casos de estudio listos para enseñar
_templates/     plantillas (plugin Templates de Obsidian)
_meta/          convenciones del vault
scripts/        publish.py
Home.md         punto de entrada
```

Es PARA (proyectos, áreas, recursos, archivo) más tres carpetas propias del trabajo de producto: diario, decisiones y portfolio.

## Cómo empezar

1. Abre la carpeta `pm-os/` como vault en Obsidian (*Open folder as vault*).
2. La configuración de `.obsidian/` ya activa Plantillas y Notas diarias.
3. Crea tu primera nota diaria. Captura en `00-inbox/`.
4. Cada viernes, usa la plantilla `weekly-review` y vacía el inbox.
5. Cada decisión relevante va en `06-decisions/` con la plantilla `decision`.

## Mover el vault a un repo privado

```bash
# 1. Crea un repo privado vacío en GitHub (p. ej. second-brain)
# 2. Desde este repo:
cp -r pm-os /ruta/a/second-brain
cd /ruta/a/second-brain
git init -b main && git add . && git commit -m "Initial vault"
git remote add origin git@github.com:kiskoros/second-brain.git
git push -u origin main
```

Después puedes quitar `pm-os/` de este repo público, dejando solo `07-portfolio/` publicado.

## Publicar al portfolio

Marca en el frontmatter de una nota `publish: true` y ejecuta:

```bash
python3 scripts/publish.py ../portfolio          # simulación (por defecto)
python3 scripts/publish.py ../portfolio --apply  # copia de verdad
```

Avisa si una nota publicada enlaza con una nota que no se publica (enlace roto en público).

## Plugins recomendados (opcionales)

- **Obsidian Git**: commit y push automáticos cada N minutos.
- **Dataview**: tablas vivas de proyectos, decisiones y notas por estado.
- **Calendar**: navegar notas diarias.

El vault funciona sin ninguno; los plugins solo lo hacen más cómodo.
