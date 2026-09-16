# 📓 Notebooks vs. Scripts — ¿cuál abro en cada reto?

Cada reto de las semanas 3–8 viene en **2 formatos idénticos en contenido**:

| Formato | Extensión | Cómo se ve | Úsalo si… |
|---------|-----------|------------|-----------|
| **Notebook** | `.ipynb` | Celdas con texto y código intercaladas (como un cuaderno interactivo) | Quieres leer teoría + ejecutar por partes y ver resultados bonitos |
| **Script** | `.py` | Un archivo de código normal | Prefieres correr todo de un jalón en la terminal |

Los dos hacen **lo mismo**. Elige el que mejor te acomode.

## Qué es un notebook (.ipynb) por dentro

Un notebook está lleno de **celdas** de dos tipos:

- 🟢 **Celdas de código**: Python que SÍ se ejecuta al pulsar ▶.
- 📝 **Celdas de Markdown**: texto con títulos, negritas y explicaciones. Se
  formatea al ejecutarlas pero no "hace nada".

![estructura-mental] de un notebook:

```
📝 1. Título y teoría      → léelo
▶  2. import ...           → ejecútalo
📝 3. "Carga los datos"     → lee la instrucción
▶  4. df = ...             → ejecútalo y observa la tabla
📝 5. """🚩 TODO: ..."""    → ¡AQUÍ TÚ! completa el código
▶  6. Tu solución          → ejecuta y comprueba el autochequeo
```

## Cómo usar los archivos `.py` del curso

Cada archivo está pensado para leerse **como una historia**:

1. 🧑‍🏫 El docstring de arriba te explica la teoría (tráelo a tu equipo).
2. 🗂️ Los comentarios con `# --- SECCIÓN ---` dividen el "capítulo".
3. 🚩 Cada `# TODO:` es donde debes escribir tu lógica.
4. ✅ Al final hay un **autochequeo** (`verificar_progreso()`) que te dirá si tu
   solución es válida **sin esperar al profe**.

> ⚠️ Si un archivo se queda en `NotImplementedError("🚩 TODO...")`, no es un
> error raro: **es la señal de que ahí debes trabajar tú**. Completa esa parte y
> vuelve a ejecutar.

## Regla de higiene del notebook

- Ejecuta las celdas **de arriba hacia abajo**, siempre que cambies algo.
- Si algo se "descompone", **Runtime → Restart and run all** (Colab) y listo.
- PONLES título a las celdas o usa Markdown para dejar evidencia de tu proceso:
```markdown
## Decisión del equipo
Elegimos X porque Y. Vimos en la tabla que Z.
```

> 🧪 **Reto relámpago:** abre `semana-04/reto_titanic.ipynb` y ejecuta solo las
> 3 primeras celdas. ¿Pasa el import? Ya sabes usar notebooks.