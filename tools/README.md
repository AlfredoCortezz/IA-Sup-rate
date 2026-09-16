# 🧰 tools/ — Caja de herramientas del curso

Este folder es tu **tutor personal**. Si te atascas o no entiendes algo, entra
aquí antes de preguntarle al profe (o a la IA 😉).

## Índice

| Guía | Cuándo usarla |
|------|---------------|
| [`01-git-y-github.md`](01-git-y-github.md) | Cuando haya que clonar, guardar (commit) o subir (push) tu trabajo |
| [`02-python-y-colab.md`](02-python-y-colab.md) | Cuando no sepas cómo correr los retos de Python (semanas 3–8) |
| [`03-notebooks-y-scripts.md`](03-notebooks-y-scripts.md) | Cuando no sepas qué es un `.ipynb` o cómo abrir los retos |
| [`04-nextjs-y-vercel.md`](04-nextjs-y-vercel.md) | Cuando llegues a las semanas 9–10 (Next.js y Vercel) |
| [`05-vocabulario-ia.md`](05-vocabulario-ia.md) | Cuando leas una palabra rara de la IA (token, embedding, sesgo…) |

> 💡 Consejo de equipo: el rol de **Investigador(a)** de la semana es quien
> normalmente consulta esta carpeta y explica al resto.

---

### 🔧 Solo para el/la docente

`generar-notebooks.py` regenera los `.ipynb` a partir de los `.py` de las
semanas 3–8 (así no hay que mantener el mismo contenido dos veces):

```bash
python tools/generar-notebooks.py
```

#### Control de intentos (Semanas 1 y 2)

- `semana-01/index.html` y `semana-02/dashboard-semana2.html` piden **nombre,
  equipo e integrantes** y permiten **un solo intento**.
- El intento se guarda en el `localStorage` del navegador (clave
  `ia_sem1_intento` / `ia_sem2_intento`). Funciona en Chrome, Edge y Firefox.
  ⚠️ Si el alumno usa **modo incógnito**, borra los datos del navegador o cambia
  de equipo, el control se reinicia. Para un control estricto, sírvelos desde un
  servidor o pídele que descargue el PDF y lo suba.
- El botón **“Reiniciar intento”** pide el código docente: **`PROFE2026`**
  (cámbialo en la constante `CODIGO_DOCENTE` de cada archivo si quieres).
- El **PDF** se genera con el diálogo de impresión del navegador
  (`Ctrl+P` → “Guardar como PDF”). No necesita internet ni librerías externas.