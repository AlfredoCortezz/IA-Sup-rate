# -*- coding: utf-8 -*-
# %% [markdown]
# # 📈 Semana 3 — Regresión Lineal: adivina tu calificación
#
# > 📍 **¿Atascado?** Pistas: `tools/pistas/semana-03.md` · Autochequeo: `python autochequeo.py`
#
# **¿Qué vas a aprender hoy?**
# A pedirle a una computadora que **prediga un número**. Por ejemplo: "si
# estudio 6 horas, ¿cuánto saco?".
#
# ## La analogía 🎯
# Imagina que pones 20 puntos en una gráfica (horas de estudio vs. calificación)
# y luego pasas una **regla** por en medio, lo más pegada posible a los puntos.
# Esa recta es tu "modelo": sirve para leer cuánto sacarías con CUALQUIER
# número de horas, incluso uno que nunca viste.
#
# $$calificacion = \text{ordenada} + \text{pendiente} \times horas$$
#
# - La **ordenada** (intercepto) es lo que sacas con 0 horas.
# - La **pendiente** es cuánto sube tu nota por cada hora extra.
#
# ## Pasos de hoy
# 1. Crear un dataset (datos inventados pero realistas).
# 2. Explorarlo con pandas y dibujarlo.
# 3. Separar features (X) y respuesta (y).
# 4. Entrenar el modelo y evaluarlo.
# 5. Interpretar la pendiente como personas de verdad.
#
# > 🚩 Cada bloque con **TODO** es tuyo. Las demás celdas ya están listas.

# %%
# ==============================================================
# 1) IMPORTAR LAS HERRAMIENTAS
# ==============================================================
# pandas  -> tablas de datos (DataFrame)
# numpy   -> números y matemáticas
# matplotlib -> dibujar gráficas
# train_test_split -> separar datos de entrenamiento y de prueba
# LinearRegression -> el modelo de regresión lineal
# mean_absolute_error, r2_score -> maneras de medir si el modelo es bueno
# ==============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Semilla: hace que los "datos aleatorios" siempre salgan iguales.
# Así tu resultado y el de tu compañero son comparables.
SEMILLA = 42
np.random.seed(SEMILLA)


def todo(mensaje):
    """Marca un paso pendiente. Si ves esto, ¡te toca programar a ti!"""
    raise NotImplementedError(f"🚩 TODO pendiente: {mensaje}")


# %% [markdown]
# ## 2) Crear el dataset
# Vamos a inventar 60 estudiantes. Cada fila tendrá:
# - `horas_estudio`: horas que estudió a la semana.
# - `calificacion`: su nota final (0 a 100).
#
# A propósito le metemos algo de **ruido**: en la vida real no siempre quien
# estudia más saca más. El modelo aprende la **tendencia**, no la excepción.

# %%
estudiantes = 60
horas_estudio = np.random.uniform(0, 10, estudiantes).round(1)   # de 0 a 10 h
ruido = np.random.normal(0, 6, estudiantes)                      # "suerte"

# 30 es la base; cada hora suma ~6 puntos; el ruido desordena un poco.
calificacion = 30 + 6.0 * horas_estudio + ruido
calificacion = np.clip(calificacion, 0, 100).round(1)            # límites 0–100

df = pd.DataFrame({
    "horas_estudio": horas_estudio,
    "calificacion": calificacion,
})

print("Primeras 5 filas del dataset:")
print(df.head())
print("\n¿Cuántos datos tenemos y qué promedio hay?")
print(df.describe())

# %% [markdown]
# ## 3) Dibujar los datos (siempre mira antes de modelar) 👀
# Un buen científico de datos SIEMPRE grafica primero. Si los puntos forman una
# línea, la regresión lineal tiene sentido. Si forman una nube, no.

# %%
plt.figure(figsize=(7, 4))
plt.scatter(df["horas_estudio"], df["calificacion"], alpha=0.7, color="#38bdf8")
plt.title("Horas de estudio vs. calificación")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")
plt.grid(alpha=0.3)
plt.show()

# %% [markdown]
# ## 4) Separar en X (pistas) y y (respuesta) 🚩 TODO
#
# - **X** = la "pista" que le damos al modelo (las horas de estudio).
# - **y** = lo que queremos predecir (la calificación).
#
# **Pista de sintaxis:** en scikit-learn, X debe ser una **tabla 2D**, así que
# seleccionamos columnas con doble corchete: `df[["horas_estudio"]]`.

# %%
# 🚩 TODO: crea X (la columna horas_estudio como tabla) y y (la calificación).
# Reemplaza la siguiente línea por tu código:
todo("define X = df[['horas_estudio']] y y = df['calificacion']")

# %% [markdown]
# ## 5) Entrenar con una parte y evaluar con OTRA 🚩 TODO
#
# Esto es **clave**: si dejamos al modelo ver todas las respuestas, podría
# "memorizarlas" y lucir perfecto. Entonces apartamos un 20 % para probar.
#
# - `test_size=0.2` → 20 % para prueba, 80 % para entrenar.
# - `random_state=SEMILLA` → que el reparto sea siempre igual.

# %%
# 🚩 TODO: usa train_test_split para crear X_train, X_test, y_train, y_test.
todo("X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA)")

# %% [markdown]
# ## 6) Crear y entrenar el modelo 🚩 TODO
#
# Entrenar (`fit`) es el momento en que la máquina ajusta la recta. Sí, es una
# sola línea. La magia está en entender QUÉ hace.

# %%
# 🚩 TODO: crea el modelo y entrénalo con los datos de entrenamiento.
todo("modelo = LinearRegression(); modelo.fit(X_train, y_train)")

# %% [markdown]
# ## 7) Predecir y medir el error 🚩 TODO
#
# - **MAE** = error promedio en puntos (mientras más bajo, mejor).
# - **R²** = qué tanto explica el modelo (1.0 = perfecto, 0 = no sirve).

# %%
# 🚩 TODO: predice con X_test y calcula mean_absolute_error y r2_score.
todo("y_pred = modelo.predict(X_test) y luego calcula el MAE y el R²")

# %% [markdown]
# ## 8) Interpretar el modelo (lo más importante) 🤔
# Un modelo sin interpretación es solo números. Aquí la recta tiene un
# significado real:
#
# - `modelo.coef_` → cuántos puntos sube la nota por cada hora extra.
# - `modelo.intercept_` → la nota base con 0 horas.

# %%
# 🚩 TODO: imprime el coeficiente y el intercepto, y explica con tus palabras.
# Pregunta guía para tu equipo: ¿la pendiente es realista? ¿Cuánto sacaría
# alguien que estudia 8 horas?
todo("imprime modelo.coef_ y modelo.intercept_ con una frase que los explique")

# %% [markdown]
# ## 9) Dibujar la recta sobre los puntos
# Si tu modelo es bueno, la línea debe pasar "por en medio" de la nube.

# %%
# 🚩 TODO: dibuja de nuevo el scatter y encima la recta del modelo.
# Ayuda: usa np.linspace(0, 10, 100) para crear horas de 0 a 10 y predice sobre
# ellas con modelo.predict(...). Pásale una tabla 2D.
todo("dibuja el scatter y superpón la recta de predicción")

# %% [markdown]
# ## 10) 🔥 Reto extra (equipo): segunda característica
#
# Agrega las `horas_sueno` al dataset y úsalas como segunda feature. ¿Mejora el
# R²? ¿Qué pasa si dormir mucho correlaciona con no estudiar? **Discutan.**

# %%
# 🚩 TODO (opcional): crea horas_sueno, agrégalas a X y compara el nuevo R².
print("Aquí va el reto extra ✨")

# %% [markdown]
# ## ✅ Autochequeo del equipo
# Antes de entregar, respondan en su `ENTREGA.md`:
#
# - [ ] ¿Qué significa el intercepto en ESTE problema?
# - [ ] ¿Por qué separamos datos de entrenamiento y de prueba?
# - [ ] ¿Qué pasaría si pusiéramos `test_size=0.9`? ¿Y `0.05`?
# - [ ] Nuestro MAE fue de ___ puntos y nuestro R² de ___.
# - [ ] ¿La regresión lineal serviría para predecir el precio de una casa? ¿Por qué?
#
# Cuando las 5 estén respondidas con tus palabras: **reto de la Semana 3
# superado** 🎉
