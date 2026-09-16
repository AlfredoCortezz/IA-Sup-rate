# -*- coding: utf-8 -*-
# %% [markdown]
# # 🧠 Semana 7 — Redes Neuronales: mirar números como una máquina
#
# **¿Qué vas a aprender hoy?**
# A construir tu primera **red neuronal** y ponerla a leer dígitos escritos a
# mano (el famoso dataset **MNIST**, con más de 70 000 imágenes).
#
# ## La analogía 🎯
# Una red neuronal es como un **equipo enorme de jueces diminutos** organizados
# en capas:
#
# ```
#   ENTRADA           CAPA OCULTA              SALIDA
#   (784 pixeles)     (64 "neuronas")          (10 opciones)
#
#    ▢ ▢ ▢ ▢             ◯ ◯ ◯ ◯                 0  ← "es un cero"     12 %
#    ▢ ▢ ▢ ▢   ────►     ◯ ◯ ◯ ◯   ────►         1  ← "es un uno"       3 %
#    ▢ ▢ ▢ ▢             ◯ ◯ ◯ ◯                 ...                    ...
#    ...                 ...                      7  ← "es un siete"    81 %
# ```
#
# - Cada **pixel** manda su valor a la capa oculta.
# - Cada **neurona** multiplica por unos **pesos** (números que aprende) y
#   "vota" por cada resultado.
# - La capa de salida elige el dígito más probable.
#
# Entrenar = ajustar MILLONES de pesos para acertar. Eso es todo el misterio. 🤯
#
# > ℹ️ Usamos la red neuronal de `scikit-learn` (`MLPClassifier`) porque es la
# > forma más simple de **entender** el concepto. En la industria se usan
# > TensorFlow o PyTorch (marco de trabajo de la próxima fase), pero la idea es
# > exactamente la misma: **capas, pesos y votos**.
#
# ## Pasos de hoy
# 1. Cargar MNIST (con plan B si no hay internet).
# 2. Ver los dígitos como imágenes.
# 3. Normalizar los pixeles (0 a 1 en vez de 0 a 255).
# 4. Separar entrenamiento/prueba.
# 5. Definir la red (capas y neuronas) 🚩.
# 6. Entrenar y medir precisión 🚩.

# %%
# ==============================================================
# 1) HERRAMIENTAS
# ==============================================================
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml, load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

SEMILLA = 42
np.random.seed(SEMILLA)


def todo(mensaje):
    raise NotImplementedError(f"🚩 TODO pendiente: {mensaje}")


# %% [markdown]
# ## 2) Cargar MNIST (con plan B)
# MNIST trae imágenes de 28×28 pixeles. `fetch_openml` lo descarga la primera vez
# (puede tardar un poquito). Si no hay internet, usamos `load_digits`, una
# versión miniatura de 8×8 que viene instalada con scikit-learn.
#
# > 🌐 **En Google Colab** esto funciona perfecto. En tu PC necesitas internet
# > la primera vez (luego queda guardado en caché).

# %%
try:
    print("Descargando MNIST... (la primera vez tarda)")
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="auto")
    X_todo = mnist.data.astype("float32")
    y_todo = mnist.target.astype("int")

    # Para que corra rápido en clase, usamos una muestra de 5000 imágenes.
    idx = np.random.RandomState(SEMILLA).choice(len(X_todo), 5000, replace=False)
    X_todo, y_todo = X_todo[idx], y_todo[idx]
    nombre_dataset = "MNIST real (5000 imágenes de 28x28)"
except Exception as e:
    print("No se pudo descargar MNIST. Usando load_digits (8x8). Motivo:", e)
    digitos = load_digits()
    X_todo, y_todo = digitos.data.astype("float32"), digitos.target.astype("int")
    nombre_dataset = "load_digits (1797 imágenes de 8x8)"

print("\nDataset:", nombre_dataset)
print("Forma de X:", X_todo.shape, "| Clases:", sorted(set(y_todo)))

# %% [markdown]
# ## 3) Ver los dígitos 👀
# Cada fila de X es UNA imagen aplanada (los pixeles en fila india). Para verla,
# hay que darle forma cuadrada con `.reshape(lado, lado)`.

# %%
lado = int(np.sqrt(X_todo.shape[1]))
plt.figure(figsize=(9, 3))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_todo[i].reshape(lado, lado), cmap="gray")
    plt.title(f"Es un {y_todo[i]}")
    plt.axis("off")
plt.suptitle("Primeros 10 dígitos del dataset")
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 4) Normalizar 🚩 TODO
# Los pixeles van de **0 a 255**. Las redes neuronales aprenden mejor con números
# **pequeños**, así que dividimos entre 255 para dejarlos entre 0 y 1.
#
# 🚩 Crea `X_norm = X_todo / 255.0`. (En el plan B de 8×8, `load_digits` ya viene
# de 0 a 16; igual dividan entre 16 para dejarlo entre 0 y 1. Lo dejamos simple:
# divide entre el máximo de X_todo.)

# %%
# 🚩 TODO: normaliza los datos.
todo("X_norm = X_todo / X_todo.max()")

# %% [markdown]
# ## 5) Separar entrenamiento y prueba 🚩 TODO
# Usa `stratify=y_todo`: eso garantiza que haya la misma proporción de "0", "1",
# "7", etc., tanto en entrenamiento como en prueba. **Si no, podría tocar un
# examen sin ningún 9** y el modelo fallaría injustamente.

# %%
# 🚩 TODO: train_test_split con test_size=0.2, random_state=SEMILLA y stratify.
todo("X_train, X_test, y_train, y_test = train_test_split(..., stratify=y_todo)")

# %% [markdown]
# ## 6) Definir la RED NEURONAL 🚩 TODO
#
# Aquí decides la arquitectura. En `MLPClassifier`:
#
# - `hidden_layer_sizes=(64,)` → **una** capa oculta de 64 neuronas.
#   - `(128, 64)` sería **dos** capas (128 y luego 64).
#   - Más neuronas/capas = más poder… y más riesgo de sobreajuste.
# - `activation="relu"` → la función que deja pasar "señales" fuertes.
# - `max_iter=20` → cuántas vueltas da al entrenamiento (épocas).
#   - Muy pocas → no aprende. Muchísimas → tarda y puede memorizar.
# - `random_state=SEMILLA` → resultados repetibles.
#
# **Empieza con `hidden_layer_sizes=(64,)`, `max_iter=20`. Luego experimenta.**

# %%
# 🚩 TODO: crea la red (MLPClassifier) y guárdala en 'red'.
todo("red = MLPClassifier(hidden_layer_sizes=(64,), activation='relu', max_iter=20, random_state=SEMILLA)")

# %% [markdown]
# ## 7) Entrenar la red 🚩 TODO
#
# ⏳ Puede tardar entre unos segundos y un par de minutos. Mientras entrena,
# piensa: ¿cuántos pesos está ajustando? (entrada × oculta + oculta × salida).

# %%
# 🚩 TODO: entrena con red.fit(X_train, y_train).
todo("red.fit(X_train, y_train)")

# %% [markdown]
# ## 8) Evaluar: ¿qué tan buena lectora es? 🚩 TODO
#
# - `accuracy_score` → % de dígitos bien leídos (un buen modelo pasa el 95 %).
# - `confusion_matrix` → los dígitos que más confunde (¿4 con 9? ¿3 con 8?).
# - Muestra también 5 imágenes que el modelo haya **fallado** y reflexiona.

# %%
# 🚩 TODO: predice y muestra accuracy + matriz de confusión.
todo("y_pred = red.predict(X_test); imprime accuracy_score y confusion_matrix")

# %% [markdown]
# ## 9) 🔥 Reto: experimenta con la arquitectura
# Prueba estas configuraciones y anota la precisión de cada una:
#
# | Arquitectura | max_iter | ¿Accuracy? |
# |--------------|----------|------------|
# | `(32,)` | 20 | |
# | `(64,)` | 20 | |
# | `(128, 64)` | 30 | |
# | `(256, 128, 64)` | 30 | |
#
# **Pregunta para el equipo:** ¿más grande siempre es mejor? ¿Qué pasa con el
# tiempo de entrenamiento? ¿Dónde empieza el sobreajuste?

# %%
# 🚩 TODO (opcional): recorre arquitecturas y compara accuracies.
print("Aquí va la experimentación de arquitecturas 🧪")

# %% [markdown]
# ## ✅ Autochequeo del equipo
#
# - [ ] ¿Cuántos valores de entrada tiene cada imagen y por qué?
# - [ ] ¿Qué hace una "neurona" dentro de la red?
# - [ ] ¿Por qué normalizamos los pixeles entre 0 y 1?
# - [ ] ¿Para qué sirve `stratify` en el split?
# - [ ] Nuestra mejor accuracy fue ___ %. ¿Qué dígitos confundía más?
#
# ¡Reto de la Semana 7 completado! 🎉 Ya entrenaste una red neuronal de verdad.
