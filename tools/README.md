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