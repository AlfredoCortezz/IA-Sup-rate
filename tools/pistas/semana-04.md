# 🚦 Pistas — Semana 4 · Árboles de Decisión (Titanic)

> Abre `semana-04/reto_titanic.py`, mira el TODO que te atascó y baja SOLO la
> pista que necesitas.

---

## TODO 1 — Preparar los datos

- 🚦 **1º intento:** los modelos no comen texto. Cualquier columna de texto
  (sexo, embarque) tiene que pasar de las palabras a **números**.
- 🚦 **2º intento:** la versión limpia está en el csv `titanic_limpio.csv`.
  Cárgalo y revisa con `.head()` qué columnas tiene y si hay valores vacíos.
- 🚦 **3º intento:** para "sobrevivir" decide quién falta: rellena los huecos
  con la mediana de su columna (`fillna(...)` en el cheatsheet). Guarda el
  resultado en un csv nuevo si quieres.

---

## TODO 2 — Elegir características (features)

- 🚦 **1º intento:** la pregunta del autochequeo aquí es clave: ¿"name" o
  "ticket" te servirían para **otro** pasajero? Si no, no sirven.
- 🚦 **2º intento:** `pclass`, `sex`, `age`, `fare`… son pistas que SÍ se repiten
  y generalizan.
- 🚦 **3º intento:** X = las columnas que elegiste, y = `survived`. Ojo: `sex`
  debe estar en números (ya viene codificado en la versión limpia, revisa).

---

## TODO 3 — Entrenar el árbol

- 🚦 **1º intento:** `DecisionTreeClassifier` ya está importado. Al crearlo,
  fija `random_state=42` para que te salga el mismo árbol que a tu compañero.
- 🚦 **2º intento:** dos pasos: `modelo = DecisionTreeClassifier(random_state=42)`
  y `modelo.fit(X_train, y_train)`.
- 🚦 **3º intento:** ¡prueba también con `max_depth=3`! Los árboles profundos
  se "saben de memoria" los datos (sobreajuste).

📌 **Código de referencia:**
```python
from sklearn.tree import DecisionTreeClassifier
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)
```

---

## TODO 4 — Ver el árbol como dibujo

- 🚦 **1º intento:** hay una función importada que dibuja el árbol:
  `plot_tree(...)`. Necesita el modelo como primer argumento.
- 🚦 **2º intento:** `plt.figure(figsize=(16, 8))` primero, `plot_tree(modelo,
  feature_names=..., class_names=["sobrevive", "no"] , filled=True)` después.
- 🚦 **3º intento:** guarda con `plt.savefig("arbol_semana4.png", dpi=120)`.

> Alargas el paper hasta que se lea. La raíz del árbol es la primera pregunta
> que hace el modelo.

---

## TODO 5 — Métricas y predicciones

- 🚦 **1º intento:** usa el molde de siempre: `predict` sobre test y compara con
  `accuracy_score` (y `confusion_matrix` para ver qué falla).
- 🚦 **2º intento:** el acurracy de "todos muertos" (baseline) era ~62 %. Si tu
  árbol sale por debajo, casi seguro hay sobreajuste o features mal puestas.
- 🚦 **3º intento:** confusión matrix se lee: la diagonal son los aciertos, los
  números fuera de la diagonal los errores. ¿Erra más en "sobrevive" o en
  "muere"?

---

## 🔬 Experimento de profundidad (la parte que te van a preguntar)

- 🚦 **1º intento:** crea el MISMO árbol con `max_depth` = 1, 3, 5, 10 y 20.
  Entrena y mide accuracy en train **y** en test para cada uno.
- 🚦 **2º intento:** guarda los resultados en una tabla (`pd.DataFrame`) y fíjate
  cuándo el accuracy de train se dispara mientras el de test se queda o baja.
- 🚦 **3º intento:** "¿a qué profundidad empieza a ENPEORAR a pesar de que
  entrena mejor?" → esa es tu respuesta 💡. Es sobreajuste con nombre.