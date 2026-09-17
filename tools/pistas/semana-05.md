# 🚦 Pistas — Semana 5 · KNN (Precios)

> Abre `semana-05/reto_knn.py`, mira el TODO que te atascó y baja SOLO la pista
> que necesites.

---

## TODO 1 — Preparar los datos

- 🚦 **1º intento:** tienes texto (títulos) y números. Pregúntate qué columna de
  texto puede servir para que dos viviendas sean "parecidas".
- 🚦 **2º intento:** el precio (la columna que le quieres preguntar al modelo) NO
  puede estar en X, porque sería la respuesta (`y`).
- 🚦 **3º intento:** X = columnas numéricas que miden parecido (p. ej.
  superficie, baños, etc.), y = `precio`. Revisa con `.head()` y `.isnull()`.

---

## TODO 2 — Escalar (¡importante!)

- 🚦 **1º intento:** ¿qué pasa si una columna va de 0 a 10 y otra de 1990 a
  2020? ¿Cuál manda en la "distancia"?
- 🚦 **2º intento:** usa `StandardScaler` (de `sklearn.preprocessing`). "Piensa"
  la escala con `fit_transform` sobre **train** y solo `transform` sobre test.
- 🚦 **3º intento:** copia el molde del cheatsheet 🐍 apartado 4. Si NO escalas,
  casi seguro tu MAE será un desastre.

---

## TODO 3 — Entrenar KNN

- 🚦 **1º intento:** `KNeighborsRegressor` (al ser precio, es regresión). Fíjate
  qué parámetro controla "cuántos vecinos".
- 🚦 **2º intento:** `n_neighbors=k` → `KNeighborsRegressor(n_neighbors=3)`.
  Con `random_state=42` en el `train_test_split` para que sea reproducible.
- 🚦 **3º intento:** ¿3, 5, 20, 100? Pruébalo todo en el reto extra. No uses la
  **edad** en X si una persona de 35 años y otra de 80 tendrían el precio casi
  igual; deja la decisión a tus resultados.

📌 **Por qué escalamos:** si una columna está en años (0-100) y otra en metros
cuadrados (0-300), el vecino se elige casi solo por los metros. Escalar lo
equipara.

---

## TODO 4 — ¿Cuándo escalar?**

- 🚦 **1º intento:** el `fit` del modelo y la transformación son cosas
  distintas. Primero **escala** los datos, **luego** entrena el modelo.
- 🚦 **2º intento:** haz `X_train_esc = escalador.fit_transform(X_train)` y
  `X_test_esc = escalador.transform(X_test)`, y alimenta el modelo **con esas**
  variables escaladas.

> ⚠️ **Regla de oro:** el escalador se aprende SOLO con train. Si usas test
> para aprender la escala, estás "haciendo trampa" en el examen.

---

## 🔥 Reto extra (los distintos k)

- 🚦 **1º intento:** haz un bucle con k = 1, 2, 3, 5, 10, 20, 50 y guarda en una
  lista el MAE de cada uno.
- 🚦 **2º intento:** k=1 es muy nervioso (memoriza el dato); k gigante promedia
  con todo el mundo. Busca en los resultados el punto donde deja de mejorar.
- 🚦 **3º intento:** responde POR QUÉ funciona así (para eso está el experimento).

---

## 🧠 La pregunta del autochequeo

> *"¿Por qué no usar `titulo` como feature?"* — porque cada título es único y
> no se repite: el modelo no aprende nada de general. Es distinto que usar
> "número de metros" (que se repite y aporta).