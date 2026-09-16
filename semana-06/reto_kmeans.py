# -*- coding: utf-8 -*-
# %% [markdown]
# # 🛒 Semana 6 — K-Means: segmenta a tus clientes
#
# **¿Qué vas a aprender hoy?**
# A **agrupar** cosas parecidas **SIN que nadie te diga las respuestas**. Esto se
# llama **aprendizaje no supervisado**: la máquina descubre grupos solita.
#
# ## La analogía 🎯
# Imagina que entras a un salón con 240 personas y te piden separarlas en 4
# grupos "que tengan sentido", pero NADIE te dice por qué criterio. Tú miras y
# dices: "ah, estos son jóvenes que gastan poquito, estos son ejecutivos…".
#
# K-Means hace lo mismo:
# 1. Elige **k** puntos al azar (los "centroides").
# 2. Asigna a cada cliente al centroide más cercano.
# 3. Mueve cada centroide al promedio de su grupo.
# 4. Repite hasta que ya no se muevan.
#
# ## 🧠 Diferencia clave con las semanas pasadas
#
# | Supervisado (S3–S5) | No supervisado (S6) |
# |---------------------|---------------------|
# | Le das las respuestas (etiquetas) | NO hay respuestas |
# | Aprende a predecir | Descubre patrones solito |
#
# ## Pasos de hoy
# 1. Generar datos de clientes ficticios.
# 2. Escalar (igual que en KNN, ¡las unidades importan!).
# 3. Elegir cuántos grupos (k) con el **método del codo** (elbow).
# 4. Entrenar K-Means y pintar los grupos.
# 5. **Ponerle nombre** a cada grupo (la parte de negocio).

# %%
# ==============================================================
# 1) HERRAMIENTAS
# ==============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

SEMILLA = 42
np.random.seed(SEMILLA)


def todo(mensaje):
    raise NotImplementedError(f"🚩 TODO pendiente: {mensaje}")


# %% [markdown]
# ## 2) Clientes ficticios (pero realistas)
# Generamos 240 clientes con 3 características:
# - `edad`
# - `gasto_mensual` (en $)
# - `visitas_por_mes`
#
# Los datos vienen "revueltos" de 4 grupos reales que están **escondidos**. Al
# final compararemos si K-Means los redescubrió. 🤫

# %%
# Centros "secretos" (no se los digas al modelo 😉)
centros = [
    [22,  80,  4],   # grupo A
    [30, 350, 15],   # grupo B
    [45, 900,  8],   # grupo C
    [62, 200,  2],   # grupo D
]
X, y_real = make_blobs(n_samples=240, centers=centros, cluster_std=60,
                       n_features=3, random_state=SEMILLA)

# Ajustamos las escalas para que se vean realistas
X[:, 0] = np.clip(X[:, 0], 18, 75).round(0)      # edad
X[:, 1] = np.clip(X[:, 1], 20, 1500).round(0)    # gasto mensual
X[:, 2] = np.clip(X[:, 2], 1, 25).round(0)       # visitas

df = pd.DataFrame(X, columns=["edad", "gasto_mensual", "visitas_por_mes"])
print(df.head())
print("\nResumen estadístico:")
print(df.describe().round(1))

# %% [markdown]
# ## 3) Mirar antes de agrupar 👀
# Grafiquemos `edad` vs `gasto_mensual`. ¿Se ven grupos a simple vista?

# %%
plt.figure(figsize=(7, 4.5))
plt.scatter(df["edad"], df["gasto_mensual"], alpha=0.6, color="#a78bfa")
plt.title("Clientes: edad vs. gasto mensual")
plt.xlabel("Edad")
plt.ylabel("Gasto mensual ($)")
plt.grid(alpha=0.3)
plt.show()

# %% [markdown]
# ## 4) Escalar 🚩 TODO
# `gasto_mensual` llega a 1500, mientras que `visitas` llega a 25. Sin escalar,
# el gasto aplastaría a las demás variables en el cálculo de distancia.
#
# **Pista:** reutiliza lo que aprendiste en la Semana 5 → `StandardScaler`.

# %%
# 🚩 TODO: escala df en una variable df_escalado (usa fit_transform).
todo("escalador = StandardScaler(); df_escalado = escalador.fit_transform(df)")

# %% [markdown]
# ## 5) ¿Cuántos grupos? El método del codo 🚩 TODO
#
# Probamos k = 2, 3, 4, 5, 6, 7, 8 y guardamos la **inercia** (qué tan
# "apretados" quedan los grupos; más bajo = más compacto). Al graficarla, a
# veces se forma un "codo" (una esquina): ese suele ser el mejor k.
#
# **Pista:** `KMeans(n_clusters=k, random_state=SEMILLA, n_init=10).fit(...)`
# y luego lee `modelo.inertia_`.

# %%
# 🚩 TODO: recorre k de 2 a 8, guarda la inercia y dibuja el codo.
todo("haz el bucle de k, guarda inercias y grafica inercia vs k")

# %% [markdown]
# ## 6) Entrenar K-Means con el k elegido 🚩 TODO
#
# Elige tu k del codo (aquí los datos tienen 4 grupos escondidos). Entrena,
# guarda las etiquetas en `df["cluster"]` y **pinta cada cluster de un color**.
# Opcional: marca los centroides con una "X".

# %%
# 🚩 TODO: entrena KMeans con tu k, asigna df["cluster"] = modelo.labels_ y grafica.
todo("entrena KMeans, asigna etiquetas al DataFrame y pinta los clusters")

# %% [markdown]
# ## 7) Interpretar: ponle nombre a cada grupo 🚩 TODO
#
# Esto es lo que le importa a la empresa. Calcula el **promedio por cluster** con
# `df.groupby("cluster").mean()` y, con esos números, **bautiza** cada segmento.
#
# Ejemplos de nombres: "Estudiantes", "Cazadores de ofertas", "Ejecutivos",
# "Jubilados tranquilos". Los nombres dependen de TUS datos.

# %%
# 🚩 TODO: imprime el promedio por cluster y escribe el nombre de cada uno.
todo("df.groupby('cluster').mean() y pon un nombre razonado a cada cluster")

# %% [markdown]
# ## 8) 🔥 Reto extra
# 1. Calcula el `silhouette_score` para varios k. Mientras más cercano a 1,
#    mejor están separados los grupos. ¿Coincide con tu codo?
# 2. Compara tus clusters con `y_real` (la respuesta secreta). ¿Acertó K-Means?

# %%
# 🚩 TODO (opcional): silhouette_score y comparación con y_real.
print("Reto extra de clustering ✨")

# %% [markdown]
# ## ✅ Autochequeo del equipo
#
# - [ ] ¿Qué diferencia hay entre aprendizaje supervisado y no supervisado?
# - [ ] ¿Qué es un centroide?
# - [ ] ¿Por qué el codo sugiere un k "óptimo"?
# - [ ] Nombres que le pusimos a nuestros clusters: ___.
# - [ ] Una empresa, ¿para qué usaría esto? Den un ejemplo real.
#
# ¡Reto de la Semana 6 completado! 🎉
