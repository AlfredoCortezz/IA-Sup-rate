# -*- coding: utf-8 -*-
# %% [markdown]
# # 🎬 Semana 5 — K-Nearest Neighbors (KNN): el "club de los parecidos"
#
# > 📍 **¿Atascado?** Pistas: `tools/pistas/semana-05.md` · Autochequeo: `python autochequeo.py`
#
# **¿Qué vas a aprender hoy?**
# A recomendar cosas usando una idea sencillísima: **"dime con quién andas y te
# diré quién eres"**. Si dos películas se parecen mucho, probablemente te gusten
# las dos.
#
# ## La analogía 🎯
# KNN = "los **K vecinos más cercanos**". Para adivinar algo de una película
# nueva, miro las **K películas más parecidas** y me fijo en lo que opinan.
#
# - Si quiero adivinar el rating → promedio el rating de sus vecinas.
# - Si quiero recomendarla → devuelvo las vecinas más cercanas.
#
# ## ⚠️ El detalle que lo cambia todo: las ESCALAS
# Imaginemos que comparamos `year` (de 1990 a 2020) contra `accion` (de 0 a 10).
# ¡El año tiene números MUCHÍSIMO más grandes! Entonces "distancia" se mediría
# casi solo por el año, y las demás características no contarían.
#
# **Solución:** escalar todo al mismo rango con `StandardScaler`. Por eso KNN
# casi siempre necesita escalado.
#
# ## Pasos de hoy
# 1. Crear un mini-catálogo de películas.
# 2. Escalar las características.
# 3. Encontrar las películas más parecidas a una que nos gusta (KNN).
# 4. Predecir el rating de una película no vista.

# %%
# ==============================================================
# 1) HERRAMIENTAS
# ==============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors, KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

SEMILLA = 42
np.random.seed(SEMILLA)


def todo(mensaje):
    raise NotImplementedError(f"🚩 TODO pendiente: {mensaje}")


# %% [markdown]
# ## 2) Nuestro catálogo de películas 🍿
# Cada película se describe con "qué tanto" tiene de cada género (0 a 10) y su
# rating (0 a 10). Tú puedes añadir tus películas favoritas al final.

# %%
catalogo = pd.DataFrame({
    "titulo":   ["Toy Story", "Titanic", "Rápidos y Furiosos", "El Rey León",
                 "Matrix", "La La Land", "John Wick", "Buscando a Nemo",
                 "El Padrino", "Interestelar", "Avengers", "Coco",
                 "Rocky", "Amélie", "Top Gun", "Spiderman"],
    "year":     [1995, 1997, 2001, 1994,
                 1999, 2016, 2014, 2003,
                 1972, 2014, 2012, 2017,
                 1976, 2001, 1986, 2002],
    "accion":   [7, 5, 9, 5,
                 9, 3, 10, 4,
                 4, 7, 9, 4,
                 8, 2, 9, 9],
    "comedia":  [9, 3, 2, 8,
                 3, 7, 1, 8,
                 3, 2, 4, 9,
                 2, 8, 2, 4],
    "romance":  [2, 10, 2, 3,
                 2, 9, 1, 1,
                 5, 6, 3, 3,
                 2, 8, 3, 5],
    "rating":   [8.3, 7.9, 6.8, 8.5,
                 8.7, 8.0, 7.4, 8.1,
                 9.2, 8.6, 7.0, 8.4,
                 8.1, 8.3, 6.9, 7.3],
})
print(catalogo)
print("\nNuestro catálogo tiene", len(catalogo), "películas.")

# %% [markdown]
# ## 3) Elegir las características 🚩 TODO
#
# Antes de medir distancias debemos decidir **qué describe** a una película.
# Usaremos: `year`, `accion`, `comedia`, `romance`.
#
# **Nota:** NO usamos `titulo` (es texto) ni `rating` (es justo lo que queremos
# predecir en el paso 5).

# %%
# 🚩 TODO: crea la lista CARACTERISTICAS y una tabla X con esas columnas.
todo("CARACTERISTICAS = ['year','accion','comedia','romance']; X = catalogo[CARACTERISTICAS]")

# %% [markdown]
# ## 4) Escalar 🚩 TODO
#
# Recuerda el problema de las escalas. Aplicamos `StandardScaler` que convierte
# cada columna a "cuántas desviaciones estándar" del promedio. Todas quedan
# comparables.
#
# **Ojo:** `fit_transform` en el catálogo (aprende la escala y la aplica). Si
# luego quieres escalar una película NUEVA, usa solo `transform` (con la misma
# escala aprendida).

# %%
# 🚩 TODO: crea el escalador, aprende y transforma X en X_escalado.
todo("escalador = StandardScaler(); X_escalado = escalador.fit_transform(X)")

# %% [markdown]
# ## 5) "Dime tus 3 películas vecinas" 🚩 TODO
#
# Con `NearestNeighbors(n_neighbors=3)` y `.fit(X_escalado)` podemos preguntar
# por las más cercanas a cualquier película.
#
# **Pista:** `modelo.kneighbors([vector])` devuelve distancias e índices. Usa
# `.iloc[índice]` para sacar el título.

# %%
# 🚩 TODO: entrena NearestNeighbors con k=3 y encuentra las vecinas de "Matrix".
todo("vecinos = NearestNeighbors(n_neighbors=3).fit(X_escalado); imprime las 3 más parecidas a Matrix")

# %% [markdown]
# ## 6) Predecir el rating de una película no vista 🚩 TODO
#
# Ahora usamos `KNeighborsRegressor`: para predecir el rating de una película
# desconocida, promedio el rating de sus películas vecinas.
#
# 🚩 Pasos:
# 1. Separa `y = catalogo["rating"]` y haz `train_test_split`.
# 2. Crea `KNeighborsRegressor(n_neighbors=3)` y entrena con los datos escalados.
# 3. Predice y mide el `mean_absolute_error`.
#
# ⚠️ Recuerda escalar X_train y X_test con el MISMO escalador (fit en train,
# transform en ambos).

# %%
# 🚩 TODO: entrena el regresor KNN y reporta su MAE.
todo("prepara X_train/X_test, escala, entrena KNeighborsRegressor y calcula el MAE")

# %% [markdown]
# ## 7) Nuestra función de recomendación 🚩 TODO
#
# Une todo: dada una película del catálogo, devuelve títulos parecidos con su
# rating, **sin incluirla a ella misma** (¡porque siempre se parecerá a sí misma
# con distancia 0!).

# %%
# 🚩 TODO: completa la función recomendar(titulo, k=3).
def recomendar(titulo, k=3):
    # 1) saca el índice de esa película
    # 2) pide a KNN sus k+1 vecinos (el +1 es porque aparecerá ella misma)
    # 3) imprime las recomendaciones (salta la primera, que eres tú)
    todo("implementa recomendar(): busca el índice, saca vecinos y muestra títulos")


# %% [markdown]
# ## 8) 🔥 Reto extra
# Prueba `k=1`, `k=3` y `k=7`. ¿Cambian las recomendaciones? ¿Cuál se siente
# "mejor" y por qué? **Aquí no hay una única respuesta correcta**; argumenta.

# %%
# 🚩 TODO (opcional): prueba distintos valores de k y compara.
print("Reto extra de KNN ✨")

# %% [markdown]
# ## ✅ Autochequeo del equipo
#
# - [ ] ¿Por qué KNN necesita escalar los datos? Explícalo con el año vs. el género.
# - [ ] ¿Qué pasa si pongo `k=1`? ¿Y si pongo un `k` enorme?
# - [ ] Nuestro MAE fue ___ .
# - [ ] ¿Por qué no usamos `titulo` como característica?
# - [ ] ¿Se te ocurre una app real que use este método? ¿Cuál?
#
# ¡Reto de la Semana 5 completado! 🎉
