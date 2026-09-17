# -*- coding: utf-8 -*-
# %% [markdown]
# # 🌳 Semana 4 — Árbol de Decisión: ¿sobrevivirías al Titanic? 🚢
#
# > 📍 **¿Atascado?** Pistas: `tools/pistas/semana-04.md` · Autochequeo: `python autochequeo.py`
#
# **¿Qué vas a aprender hoy?**
# A que la máquina decida "sí o no" haciendo **preguntas en cadena**, como en el
# juego de las 20 preguntas. Eso es un **árbol de decisión**.
#
# ## La analogía 🎯
# Imagina que pierdes un objeto en tu casa. Para encontrarlo preguntas:
#
# 1. ¿Está en mi cuarto? → **Sí** → ¿Está en el escritorio? → **No** → ...
# 2. ¿Está en la sala? → **No** → ...
#
# Cada respuesta descarta un montón de posibilidades y te acerca a la
# respuesta. Un árbol de decisión hace exactamente eso:
#
# ```
#                ¿Eres mujer?  (primera pregunta, la más "divisoria")
#               /            \
#             Sí             No
#             /               \
#      ¿3ª clase?          ¿Eres niño?
#       /      \            /      \
#    Sobrev.  Murió      Sobrev.   Murió
# ```
#
# Las preguntas de arriba son las **más útiles**; las respuestas finales
# (sobrevive/muere) son las **hojas** del árbol.
#
# ## Pasos de hoy
# 1. Cargar el dataset real del Titanic.
# 2. Explorar: ¿quiénes sobrevivieron más?
# 3. Preparar los datos (quitar nulos, convertir texto a número).
# 4. Entrenar un árbol de decisión.
# 5. Medir su precisión y **dibujar el árbol** para entenderlo.
# 6. Descubrir el sobreajuste (overfitting) jugando con la profundidad.

# %%
# ==============================================================
# 1) IMPORTAR HERRAMIENTAS
# ==============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

SEMILLA = 42
np.random.seed(SEMILLA)


def todo(mensaje):
    """Marca un paso pendiente. Si esto te detiene, ¡es tu turno de programar!"""
    raise NotImplementedError(f"🚩 TODO pendiente: {mensaje}")


# %% [markdown]
# ## 2) Cargar el dataset del Titanic
# `seaborn` trae el dataset "titanic" listo para usar. Son 891 personas con
# datos como clase, sexo, edad, tarifa y si **sobrevivieron** (`survived`:
# 1 = sí, 0 = no). ¡Es historia real del naufragio de 1912!

# %%
df = sns.load_dataset("titanic")

print("Filas:", df.shape[0], "| Columnas:", df.shape[1])
print("\nAlgunas columnas:")
print(df[["survived", "pclass", "sex", "age", "fare"]].head())

# %% [markdown]
# ## 3) Explorar: ¿quién sobrevivió más? 👀
# Antes de modelar, mira los datos. Aquí hacemos `groupby` para ver los
# porcentajes de supervivencia por sexo y por clase. Este hallazgo guiará al
# árbol sin que se lo digas.

# %%
print("Supervivencia por sexo (0=murió, 1=sobrevivió):")
print(df.groupby("sex")["survived"].mean().round(3))

print("\nSupervivencia por clase social:")
print(df.groupby("pclass")["survived"].mean().round(3))

print("\n¿Faltan datos en alguna columna?")
print(df[["age", "fare", "embarked", "sex"]].isnull().sum())

# %% [markdown]
# ## 4) Preparar los datos 🚩 TODO
#
# Los modelos **no entienden texto**, solo números. Y **no aceptan huecos**
# (`NaN`). Así que:
#
# - Elegir las columnas útiles (**features**): `pclass`, `sex`, `age`,
#   `sibsp`, `parch`, `fare`.
# - Convertir `sex` a números: `male` → 0, `female` → 1.
# - Rellenar o eliminar las edades faltantes (hay muchos `NaN` en `age`).
#
# **Pista:** `df["sex"].map({"male": 0, "female": 1})` convierte el texto a
# números. Para los nulos, `df.dropna(...)` borra filas o `df["age"].fillna(...)`
# rellena con un valor (por ejemplo, la mediana: `df["age"].median()`).

# %%
# 🚩 TODO: 1) selecciona las features, 2) convierte sex, 3) maneja los NaN.
# Empieza así y completa lo que falta:
todo("crea 'datos' con las columnas útiles, convierte sex y maneja los NaN")

# %% [markdown]
# ## 5) Separar X (pistas) e y (respuesta) 🚩 TODO
#
# - **X** = todas las columnas menos `survived`.
# - **y** = `survived` (lo que queremos predecir).
#
# Y luego reparte entrenamiento/prueba con `train_test_split`.

# %%
# 🚩 TODO: define X e y, y sepáralos en X_train, X_test, y_train, y_test.
todo("X = datos.drop('survived', axis=1); y = datos['survived']; y el split 80/20")


# %% [markdown]
# ## 6) Crear el árbol y entrenarlo 🚩 TODO
#
# `max_depth` es la **profundidad máxima** del árbol: cuántas preguntas encadena.
# - Muy chico (1–2) → el árbol no aprende (subentrenamiento).
# - Muy grande (sin límite) → se memoriza los datos (¡sobreajuste!).
#
# Empieza con `max_depth=3` y analiza. Recuerda fijar `random_state=SEMILLA`.

# %%
# 🚩 TODO: crea DecisionTreeClassifier con max_depth=3 y entrénalo.
todo("arbol = DecisionTreeClassifier(max_depth=3, random_state=SEMILLA); arbol.fit(...)")

# %% [markdown]
# ## 7) Evaluar el modelo 🚩 TODO
#
# - `accuracy_score` → % de aciertos (cuidado: predecir "todos mueren" ya da ~62 %).
# - `confusion_matrix` → tabla de aciertos/errores por clase.
# - `classification_report` → precisión y recall detallados.

# %%
# 🚩 TODO: predice con X_test y muestra accuracy, matriz de confusión y reporte.
todo("y_pred = arbol.predict(X_test); imprime accuracy_score, confusion_matrix y classification_report")

# %% [markdown]
# ## 8) ¡Dibujar el árbol! 🌳 (la parte divertida)
# `plot_tree` dibuja las preguntas y las hojas con colores. Aquí VES cómo
# piensa el modelo, algo que con una red neuronal no puedes.

# %%
# 🚩 TODO: usa plot_tree con las columnas de X como nombres de features.
# Sugerencia: plt.figure(figsize=(14, 7)); plot_tree(arbol, feature_names=list(X.columns),
# class_names=["No","Sí"], filled=True); plt.savefig("arbol_titanic.png"); plt.show()
todo("dibuja el árbol con plot_tree y guárdalo con plt.savefig('arbol_titanic.png')")

# %% [markdown]
# ## 9) 🔥 Reto: cazar el sobreajuste
# Entrena árboles con `max_depth` = 1, 2, 3, 5, 10 y **sin límite**. Compara la
# precisión en entrenamiento vs. en prueba.
#
# **Pregunta clave:** el de profundidad 10 acierta casi el 100 % en
# entrenamiento pero menos en prueba. ¿Por qué? (pista: memorizar vs. entender).

# %%
# 🚩 TODO: bucle sobre profundidades y tabla comparando train vs test.
print("Aquí va el experimento de sobreajuste 🔬")

# %% [markdown]
# ## ✅ Autochequeo del equipo
# Responde en tu `ENTREGA.md`:
#
# - [ ] ¿Cuál fue la primera pregunta (raíz) de tu árbol y por qué crees que la eligió?
# - [ ] ¿Qué significa una "hoja" del árbol?
# - [ ] Nuestro accuracy fue ___ %. ¿Es mejor que "decir siempre que no sobrevivió" (62 %)?
# - [ ] ¿Qué le pasa al modelo con `max_depth=20`?
# - [ ] ¿Por qué no podemos usar `name` o `ticket` como feature?
#
# ¡Con esto cierras el reto de la Semana 4! 🎉
