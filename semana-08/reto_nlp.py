# -*- coding: utf-8 -*-
# %% [markdown]
# # 💬 Semana 8 — NLP: ¿esa reseña es buena o mala?
#
# > 📍 **¿Atascado?** Pistas: `tools/pistas/semana-08.md` · Autochequeo: `python autochequeo.py`
#
# **¿Qué vas a aprender hoy?**
# A enseñarle a una computadora a **entender el sentimiento** de un texto. Esto
# es **Procesamiento de Lenguaje Natural (NLP)**, la tecnología detrás de los
# filtros de spam, los traductores y los chatbots.
#
# ## El problema 🎯
# Las computadoras no entienden letras: entienden **números**. Entonces, ¿cómo
# convertimos "me encantó esta película" en números?
#
# ## La solución en 3 pasos
#
# 1. **Tokenizar**: partir el texto en palabras.
# 2. **Vectorizar**: contar qué tan importante es cada palabra en el texto.
#    - `CountVectorizer`: cuenta cuántas veces aparece cada palabra.
#    - `TfidfVectorizer`: además, resta importancia a palabras comunes como
#      "de", "la", "que" (que aparecen en TODAS las reseñas y no distinguen nada).
# 3. **Clasificar**: un modelo mira esos números y decide 📈 positiva o 📉 negativa.
#
# ```
# "¡Me encantó, la actuación fue brutal!"
#        │ tokenizar + vectorizar
#        ▼
# [0.3, 0, 0.8, 0.5, ...]  →  Modelo  →  POSITIVA ✅
# ```
#
# ## Pasos de hoy
# 1. Cargar reseñas etiquetadas (positivas/negativas).
# 2. Separar entrenamiento y prueba.
# 3. Vectorizar el texto 🚩.
# 4. Entrenar un clasificador 🚩.
# 5. Predecir reseñas NUEVAS escritas por ustedes 🚩.

# %%
# ==============================================================
# 1) HERRAMIENTAS
# ==============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

SEMILLA = 42
np.random.seed(SEMILLA)


def todo(mensaje):
    raise NotImplementedError(f"🚩 TODO pendiente: {mensaje}")


# %% [markdown]
# ## 2) Nuestro pequeño dataset de reseñas
# Son pocas (por eso las compartimos aquí), pero suficientes para aprender.
# La etiqueta `sentimiento` es **1 = positiva** y **0 = negativa**.
#
# > 🔥 Reto de equipo: cada integrante añade **2 reseñas propias** (una buena y
# > una mala, de un producto o película que conozca) al final de la lista.

# %%
resenas = pd.DataFrame({
    "texto": [
        "Me encantó la película, la actuación fue increíble y la historia atrapante",
        "Una obra maestra, salí del cine feliz y con ganas de verla otra vez",
        "Excelente servicio, el paquete llegó rapidísimo y en perfecto estado",
        "El producto es buenísimo, superó todas mis expectativas, muy recomendado",
        "Increíble calidad, se nota que está bien hecho, valió cada peso",
        "La pasé genial, el ambiente estuvo divertidísimo toda la noche",
        "Superó lo que esperaba, el equipo me atendió con mucha amabilidad",
        "Muy buena compra, funciona perfecto y llegó antes de lo prometido",
        "No me gustó nada, la historia era aburrida y los actores flojos",
        "Fue lo peor, perdí mi tiempo y mi dinero con esta basura de película",
        "Pésimo servicio, nadie me atendió y el paquete llegó roto y tarde",
        "El producto es malísimo, se rompió al segundo día, no lo compren",
        "Una decepción total, esperaba mucho más y me quedé dormido de aburrido",
        "Terrible experiencia, todo salió mal y nadie se hizo responsable",
        "Mala calidad, muy caro para lo que ofrece, no volvería a pagar por esto",
        "No lo recomiendo para nada, el resultado fue un desastre completo",
    ],
    "sentimiento": [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
})

print(resenas)
print("\n¿Cuántas positivas y cuántas negativas?")
print(resenas["sentimiento"].value_counts().rename({1: "positivas", 0: "negativas"}))

# %% [markdown]
# ## 3) Separar entrenamiento y prueba 🚩 TODO
# `X` son los textos; `y` son las etiquetas (1/0). Usa `train_test_split` con
# `test_size=0.3` y `random_state=SEMILLA`.
#
# ⚠️ Con datasets chiquitos, a veces el examen cae con puras frases fáciles (o
# difíciles). Si la precisión sale rara, prueba cambiar el `random_state`.

# %%
# 🚩 TODO: define X, y y haz el split.
todo("X = resenas['texto']; y = resenas['sentimiento']; train_test_split(..., test_size=0.3)")

# %% [markdown]
# ## 4) Vectorizar el texto 🚩 TODO
#
# **La regla de oro:** el vectorizador se **entrena** (`fit`) SOLO con el texto de
# entrenamiento. Si lo entrenamos con todo, estaríamos "haciendo trampa": el
# modelo ya habría visto palabras del examen.
#
# - `vectorizador.fit_transform(X_train)` → aprende el vocabulario y convierte.
# - `vectorizador.transform(X_test)` → usa el MISMO vocabulario, sin re-aprender.
#
# Prueba con `TfidfVectorizer()` (mejor) o `CountVectorizer()` (más simple).

# %%
# 🚩 TODO: crea el vectorizador, aprende con X_train y transforma X_test.
todo("vectorizador = TfidfVectorizer(); X_train_vec = vectorizador.fit_transform(X_train); X_test_vec = vectorizador.transform(X_test)")

# %% [markdown]
# ## 5) Entrenar el clasificador 🚩 TODO
#
# `MultinomialNB` (Naive Bayes) es perfecto para texto: rápido y sorprendentemente
# bueno. Es como un detective que aprende qué palabras son "sospechosas" de cada
# clase.
#
# **Pista:** entrena con los datos vectorizados, no con el texto.

# %%
# 🚩 TODO: crea MultinomialNB y entrénalo con X_train_vec, y_train.
todo("modelo = MultinomialNB(); modelo.fit(X_train_vec, y_train)")

# %% [markdown]
# ## 6) Evaluar 🚩 TODO
#
# - `accuracy_score` → % de aciertos.
# - `confusion_matrix` → cuántas positivas se le escaparon como negativas (¡lo
#   más caro en la vida real!).

# %%
# 🚩 TODO: predice sobre X_test_vec e imprime accuracy y matriz de confusión.
todo("y_pred = modelo.predict(X_test_vec); imprime accuracy_score y confusion_matrix")

# %% [markdown]
# ## 7) Probar con reseñas NUEVAS 🚩 TODO
#
# Aquí está la magia: escribe 3 frases que el modelo **nunca vio** y pídele su
# sentimiento. OJO: debes transformarlas con el MISMO vectorizador.
#
# **Pista:** `modelo.predict(vectorizador.transform(["tu frase aquí"]))`
# devuelve `array([1])` o `array([0])`.

# %%
nuevas = [
    "La verdad me pareció entretenida y bien hecha, la recomiendo",
    "Fue una pérdida de tiempo, no la terminaría ni pagando",
    "Me dejó sin palabras, lo mejor que he visto este año",
]

# 🚩 TODO: transforma 'nuevas' y muestra la predicción de cada una con su frase.
todo("recorre nuevas, predice con el modelo y muestra POSITIVA/NEGATIVA por frase")

# %% [markdown]
# ## 8) ¿Qué palabras "delatan" cada sentimiento? 🔍
# Naive Bayes guarda la probabilidad de cada palabra por clase. Podemos sacarlas
# para ver qué entendió el modelo. Es la parte más honesta de la IA: **podemos
# inspeccionar lo que aprendió**.
#
# 🚩 Reto: imprime las 5 palabras más asociadas a POSITIVA y a NEGATIVA usando
# `vectorizador.get_feature_names_out()` y `modelo.feature_log_prob_`.

# %%
# 🚩 TODO (opcional): muestra las palabras más "positivas" y más "negativas".
print("Reto extra de NLP ✨")

# %% [markdown]
# ## ✅ Autochequeo del equipo
#
# - [ ] ¿Por qué el texto debe convertirse en números?
# - [ ] ¿Qué diferencia hay entre `CountVectorizer` y `TfidfVectorizer`?
# - [ ] ¿Por qué `fit` va solo en entrenamiento? ¿Qué pasaría si no?
# - [ ] Nuestra accuracy fue ___ %.
# - [ ] ¿Una palabra sola puede "delatar" el sentimiento? Den un ejemplo.
# - [ ] ¿Por qué este sistema podría fallar con sarcasmo? 🤔
#
# ¡Felicidades! Terminaste la fase de Machine Learning 🎓
