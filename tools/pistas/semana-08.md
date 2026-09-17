# 🚦 Pistas — Semana 8 · NLP (Naive Bayes)

> Abre `semana-08/reto_nlp.py`, mira el TODO que te atascó y baja SOLO la pista
> que necesites.

---

## TODO 1 — Preparar los datos

- 🚦 **1º intento:** tienes texto + sentimiento (1 = positiva, 0 = negativa).
  Los modelos no leen palabras: hay que **convertir el texto a números**.
- 🚦 **2º intento:** `TfidfVectorizer` está importada. Crea una instancia y
  úsala para "aprender" del train con `fit_transform`.
- 🚦 **3º intento:** el vectorizador convierte cada reseña en un vector de
  números que miden la importancia de cada palabra. Y recuerda: aprende SOLO
  con train (regla de oro), y para test usa solo `transform`.

---

## TODO 2 — Entrenar y predecir

- 🚦 **1º intento:** este modelo adivina la categoría de un texto → es de
  *clasificación*. Usa `MultinomialNB` (ya importado).
- 🚦 **2º intento:** `modelo = MultinomialNB()` → `modelo.fit(X_train_vec, y_train)`.
  Nota: le pasas los vectores, no el texto crudo.
- 🚦 **3º intento:** predice con `modelo.predict(X_test_vec)` sobre los vectores
  de test.

---

## TODO 3 — Métricas

- 🚦 **1º intento:** es clasificación binaria: usa `accuracy_score`,
  `confusion_matrix` y `classification_report` (ya importadas).
- 🚦 **2º intento:** con solo 16 reseñas y split 70/30, espera un accuracy de
  ~75–90 %. Si te sale 50 %, casi seguro invertiste las etiquetas de positivos
  y negativos.
- 🚦 **3º intento:** lee la matriz de confusión: ¿falla más en negativas o en
  positivas? Eso te da un párrafo para escribir en tu ENTREGA.md.

---

## TODO 4 — Probar frases nuevas

- 🚦 **1º intento:** la misma receta: `vectorizador.transform([frase])` y
  `modelo.predict(...)`.
- 🚦 **2º intento:** prueba frases positivas, negativas y una con sarcasmo (ej.
  "qué maravilla, se rompió al primer uso"). Fíjate QUÉ dice el modelo.
- 🚦 **3º intento:** el vecino de arriba te da oro: "por qué falla con el
  sarcasmo" es LA respuesta que busca la última pregunta del reto.

---

## Todo final — Palabras clave

- 🚦 **1º intento:** el modelo guarda `feature_log_prob_` (probabilidad de cada
  palabra por clase).
- 🚦 **2º intento:** `modelo.feature_log_prob_` es una matriz 2×N: fila 0 =
  negativas, fila 1 = positivas. Ordena y muestra las top 5 de cada una.
- 🚦 **3º intento:**
  ```python
  palabras = vectorizador.get_feature_names_out()
  top_pos = modelo.feature_log_prob_[1].argsort()[::-1][:5]
  top_neg = modelo.feature_log_prob_[0].argsort()[::-1][:5]
  ```
  ¿Coinciden con lo que tú creerías que dice una buena o mala reseña? Coméntalo.

---

## 🧠 Preguntas típicas

- **¿Textos → números?** Con `CountVectorizer` (solo cuenta) o `TfidfVectorizer`
  (resta peso a palabras que están en todos lados, como "de", "la", "que").
- **¿Tfidf vs Count?** Tfidf suele ganar porque reduce palabras vacías sin
  tener que montar una lista a mano.
- **¿Por qué `fit` solo en train?** Si el vectorizador viera las palabras del
  examen, sabría "filtrar" y el test dejaría de ser un examen real. Misma regla
  de oro que en el escalado de la Semana 5.

> 💡 Recuerda: los vectores que aprende `fit_transform` sobre train son la única
> escala permitida para test. Siempre `transform` (sin fit) ahí.