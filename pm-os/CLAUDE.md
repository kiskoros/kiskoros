# Instrucciones para Claude en este vault

Este es el vault de Obsidian de un PM. Lee `_meta/conventions.md` antes de crear o mover notas.

## Reglas

- Idioma por defecto: español. Nombres de carpetas y archivos en minúsculas con guiones, sin acentos ni espacios.
- Toda nota nueva lleva frontmatter con `type`, `status`, `created`, `publish` y `confidential`.
- `publish` es `false` salvo que el usuario diga expresamente que algo es público.
- Nunca pongas `publish: true` por iniciativa propia.
- Nunca incluyas en notas publicables nombres de clientes, datos personales de terceros, cifras internas ni citas literales de entrevistas sin pseudonimizar.
- Usa enlaces `[[wikilink]]` entre notas. No dejes notas huérfanas: enlaza desde `Home.md` o desde un MOC.
- Las decisiones van en `06-decisions/` con la plantilla `decision`. No las entierres en notas de reunión.
- No borres notas; muévelas a `04-archive/`.

## Flujos frecuentes

- **Revisión semanal**: crea `05-journal/weekly/AAAA-Wnn.md` desde `_templates/weekly-review.md`, resumiendo las notas diarias de la semana.
- **Vaciar inbox**: propón destino (proyecto, área, recurso, archivo) para cada nota de `00-inbox/` y espera confirmación antes de mover.
- **Caso de estudio**: a partir de un proyecto y sus decisiones, redacta un borrador en `07-portfolio/` con la plantilla `case-study`, anonimizado, con `publish: false` hasta revisión humana.
