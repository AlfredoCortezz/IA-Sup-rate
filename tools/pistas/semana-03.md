# 🚦 Pistas — Semana 3 · Regresión Lineal

> Abre el archivo `semana-03/reto_regresion_lineal.py`, mira el TODO que te
> atascó y baja SOLO la pista que necesitas. Cada nivel da un poco más de pista.

---

## TODO 1 — Definir `X` e `y`

- 🚦 **1º intento:** el "X" son las pistas (horas de estudio) y el "y" es lo que
  quieres predecir (la calificación). Piensa en 1D vs 2D.
- 🚦 **2º intento:** scikit-learn quiere una "tabla" 2D para X. ¿Cómo consigues
  una columna como tabla y no como serie? (Mira el cheatsheet 🐍).
- 🚦 **3º intento:** `X = df[["horas_estudio"]]` y `y = df["calificacion"]`.
  Doble corchete = tabla (2D); un corchete = serie (1D).

📌 **Cómo comprobarlo tú mismo:** `autochequeo` (ver README) o el error
`Expected 2D array` (→ `tools/06-errores-comunes.md` nº 1).

---

## TODO 2 — Separar train/test

- 🚦 **1º intento:** a entrenar le toca la mayoría; a probar le toca probar.
- 🚦 **2º intento:** la función se llama `train_test_split`, recibe `X`, `y`,
  un `test_size` y un `random_state`. Te devuelve 4 variables.
- 🚦 **3º intento:**
  ```python
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=SEMILLA)
  ```

📌 Prueba a cambiar `test_size` a `0.05` o `0.9` y observa qué pasa con las
métricas. Es el experimento que te preguntarán en el autochequeo.

---

## TODO 3 — Crear y entrenar el modelo

- 🚦 **1º intento:** la clase está importada: `LinearRegression`. Primero
  **creas** el modelo, luego lo **entrenas** con `.fit`.
- 🚦 **2º intento:** dos pasos escritos en la misma línea escribe:
  `modelo = LinearRegression()` y `modelo.fit(X_train, y_train)`.
- 🚦 **3º intento:** ¡eso es todo! No le pasas test al `fit`, solo `X_train` e
  `y_train`.

---

## TODO 4 — Predecir y medir el error (MAE)

- 🚦 **1º intento:** primero predice sobre `X_test` con `.predict(...)`. Después
  compara con `y_test` usando la métrica que ya está importada.
- 🚦 **2º intento:** `y_pred = modelo.predict(X_test)` y luego
  `mae = mean_absolute_error(y_test, y_pred)`.
- 🚦 **3º intento:** quieres un resultado al estilo *"MAE: 4.71 puntos"*, así que
  imprime con `print(f"MAE: {mae:.2f} puntos")`.

---

## TODO 5 — Imprimir coeficiente e intercepto

- 🚦 **1º intento:** hay dos atributos del modelo: la "pendiente" (`coef_`) y la
  "ordenada" (`intercept_`).
- 🚦 **2º intento:** `modelo.coef_` te da una lista con un número (pendiente);
  `modelo.intercept_` un único número (la base).
- 🚦 **3º intento:** imprime y **EXPLICA** en español qué significan. Ejemplo:
  "por cada hora extra de estudio, la nota sube ~X puntos".

> 🤔 La pregunta del autochequeo — *"¿qué significa el intercepto?"* — tiene la
> respuesta en tu propia explicación. No la saltes: es lo que sabes de verdad.

---

## Todo final — R²

- 🚦 **1º intento:** ya calculaste el MAE. Ahora mide cuánto variación explica
  el modelo, con la métrica importada `r2_score`.
- 🚦 **2º intento:** `r2 = r2_score(y_test, y_pred)`. Imprímelo con 4 decimales.
- 🚦 **3º intento:** un R² como `0.71` se lee: "el 71 % de la variación de las
  notas se explica con las horas de estudio". Escribe esa idea.

---

## 🔥 Reto extra (opcional)

- 🚦 **1º intento:** copia dentro del reto el mismo molde que usaste (train/test
  → modelo → métrica) pero cambiando la columna de pistas.
- 🚦 **2º intento:** crea un `X2` con dos columnas: `horas_estudio` y
  `horas_sueno`. ¿Bajó el MAE?
- 🚦 **3º intento:** no importa si empeora. Importa que **expliques** si añadir
  una feature mejora o no, y por qué crees que pasa. Eso es el reto.