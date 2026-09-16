# 🐍 Python y Google Colab — dónde correr tus retos (semanas 3–8)

Tienes **2 opciones**. Empieza por la que te sea más fácil.

## Opción A: Google Colab (0 instalaciones, recomendada)

Colab es un cuaderno de Python **en el navegador**, creado por Google. Corre en
la nube, no en tu PC.

1. Entra a <https://colab.research.google.com>
2. **File → Upload notebook** y sube el `.ipynb` de tu semana.
3. O abre un notebook nuevo y **pega el contenido del archivo `.py`** en celdas.
4. En cada celda de código pulsa **▶ para ejecutar** (Ctrl + Enter).
5. Las celdas se ejecutan **en orden, de arriba hacia abajo**.

> ⚠️ **Truco clave:** si te da error, vuelve a ejecutar desde arriba
> (**Runtime → Run all**). El orden de las celdas SÍ importa.

## Opción B: Python en tu PC (versión tech)

```bash
# Asegúrate de tener Python 3.10+
python --version

# Instala las bibliotecas del curso (una sola vez)
pip install numpy pandas matplotlib scikit-learn seaborn jupyter
```

Luego corre un reto así:

```bash
# Si es un archivo .py:
python reto_titanic.py

# Si es un notebook:
jupyter notebook
# se abrirá el navegador; clic en la carpeta y en el archivo
```

## 📦 Las bibliotecas (qué es cada una)

| Biblioteca | Sirve para… |
|------------|-------------|
| `pandas` | Tablas de datos (como Excel en Python). El objeto clave es el **DataFrame**. |
| `numpy` | Números y matemáticas (arrays, raíces, promedios). |
| `matplotlib` | Dibujar **gráficas** (scatter, líneas, barras). |
| `scikit-learn` (`sklearn`) | Los **modelos de IA ya hechos**: regresión, árboles, KNN, clustering, redes… |

## 🚑 Socorrista de errores frecuentes

| Error típico | Qué significa | Solución |
|--------------|---------------|----------|
| `ModuleNotFoundError: No module named 'sklearn'` | No está instalada la biblioteca | `pip install scikit-learn` (o usa Colab) |
| `NameError: name 'df' is not defined` | Usaste `df` antes de crearlo | Ejecuta la celda anterior (arriba) |
| `FileNotFoundError` | No encuentra el archivo | Revisa que estés en la carpeta correcta |
| `ValueError: could not convert string to float` | Hay texto donde el modelo espera número | Eso es EXACTAMENTE lo que verás en el reto: debes **convertir** el texto a número 🌈 |

> 🧪 **Reto relámpago:** corre `print("Hola equipo")` en Colab y en tu PC. Ya tienes tu primer ambiente de trabajo listo.