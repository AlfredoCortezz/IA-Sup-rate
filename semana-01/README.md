# Semana 1 — ¿Qué es la IA de verdad?

## Entrega de la semana

La primera semana tiene **dos entregables obligatorios** y un **punto extra**
opcional:

1. **Examen en línea** del archivo `index.html` de esta carpeta. La
   calificación la obtiene directamente el cuestionario (de 0 a 100) y se
   entrega el **reporte en PDF** con aciertos y errores.
2. **Actividad Teachable Machine**: entrenar un mini modelo de clasificación y
   entregar la evidencia (captura o enlace).
3. **Punto extra (opcional)**: corregir los errores del examen y justificar con
   fuentes verídicas la información corregida. Se suma como punto extra al
   examen, en grupo.

### Cómo realizar el examen (paso a paso)

1. Descarga el repositorio en tu laptop:
   `git clone https://github.com/AlfredoCortezz/IA-Sup-rate.git`
   (si no usas git, puedes descargar únicamente el archivo `index.html`).
2. Abre `semana-01/index.html` en tu navegador (doble clic sobre el archivo).
   La página funciona sin conexión a internet.
3. Regístrate con tu **nombre completo**, tu **equipo** y los **integrantes**
   de tu equipo.
4. Responde el cuestionario. Solo se permite **un intento**: al terminar, la
   página se bloquea automáticamente.
5. Descarga el **reporte en PDF** con el botón de la página (en el diálogo de
   impresión elige "Guardar como PDF"). Ese PDF es tu evidencia.

### Cómo realizar Teachable Machine (paso a paso)

1. Abre `https://teachablemachine.withgoogle.com`.
2. Entrena un modelo pequeño con tu cámara: 3 clases de unas 10 fotos cada una.
3. Comprueba que no es magia: es un clasificador que aprende patrones de las
   fotos, igual que el cuestionario aprende de ti.
4. Guarda una **captura o el enlace** como evidencia.

### Punto extra (opcional)

Corrige los errores que marcó tu examen y explica, con **fuentes verídicas**
(no respuestas generadas por IA), la información correcta de cada uno. Incluye
la referencia de la fuente (título, enlace o libro). Se suma como punto extra
al examen del grupo.

### Reglas importantes

- Un intento por estudiante (la página lo registra en el navegador).
- Responde con base en la teoría de `guia-semana-01.pdf` y de
  `tools/05-vocabulario-ia.md`.
- La nota del examen (0 a 100) la calcula el propio cuestionario.

## Cómo entregar (cada estudiante crea su propia rama)

Para que el docente pueda evaluarte, cada estudiante trabaja y entrega en su
**propia rama**. Ejemplo:

```bash
git clone https://github.com/AlfredoCortezz/IA-Sup-rate.git
cd IA-Sup-rate
git checkout -b tu-nombre-semana-01        # crea TU rama
# copia aquí tu reporte (ej. reporte-semana1.pdf) dentro de semana-01/
git add semana-01
git commit -m "Entrega semana 1 - <tu nombre>"
git push origin tu-nombre-semana-01
```

Después de hacer `push`, avisa al docente (puedes abrir un *pull request* o
enviar el enlace de tu rama). Recuerda: **no** hagas `push` a la rama `main`.

### Plantilla de `ENTREGA.md`

Crea este archivo en `semana-01/` con tus datos:

```markdown
# Entrega Semana 1 — Qué es la IA de verdad

**Estudiante:** <tu nombre completo>
**Equipo:** <nombre del equipo>
**Integrantes:** <nombre de los integrantes>
**Fecha:** <fecha>

## 1. Examen en línea
Nota obtenida en el cuestionario: **__/100**
Reporte del examen (`reporte-semana1.pdf`) adjunto en esta carpeta.

## 2. Actividad Teachable Machine
[enlace o captura del mini modelo]

## 3. Punto extra (opcional)
[corrección de los errores del examen con justificación y fuentes verídicas]
```

## Contenido de estudio

- `guia-semana-01.pdf` — teoría y ejercicios de la semana (parte de la guía
  oficial del curso dividida por semana).
- `tools/05-vocabulario-ia.md` — glosario del curso.