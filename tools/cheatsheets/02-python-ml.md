# 🐍 Python + Machine Learning — Cheatsheet (Semanas 3–8)

> Imprimible: una página con lo que vas a usar TODAS las semanas.

## 1. Pandas: la tabla de datos 🗃️

```python
import pandas as pd

df = pd.read_csv("datos.csv")        # cargar un CSV
df.head()                            # primeras 5 filas
df.describe()                        # estadísticas
df.isnull().sum()                    # ¿dónde faltan datos?
df["columna"]                        # serie (1D)
df[["a", "b"]]                       # tabla (2D) ← para X
df["columna"].fillna(df["columna"].median())   # rellenar nulos
df["texto"].map({"male": 0, "female": 1})      # texto → número
df.drop("columna", axis=1)           # quitar una columna
df.groupby("clave").mean()           # promedios por grupo
df["nueva"] = df["a"] + df["b"]      # crear una columna
```

## 2. El molde de TODO modelo (scikit-learn)

```python
from sklearn.model_selection import train_test_split

# 1) separar pistas (X) de respuesta (y)
X = df[["feature1", "feature2"]]
y = df["respuesta"]

# 2) partir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 3) crear, entrenar, predecir
modelo = Algo()               # LinearRegression(), DecisionTreeClassifier(), ...
modelo.fit(X_train, y_train)  # ← entrenar
y_pred = modelo.predict(X_test)
```

> `random_state=42` = mismo resultado todas las veces. **Ponlo SIEMPRE.**

## 3. Métricas que usamos en el curso 📏

| Métrica | Qué mide | ¿Bueno? |
|---------|----------|---------|
| `mean_absolute_error(y_test, y_pred)` | Error promedio en las unidades | Más bajo |
| `r2_score(y_test, y_pred)` | % de variación explicada | Más alto (max 1) |
| `accuracy_score(y_test, y_pred)` | % de aciertos | Más alto (max 1) |
| `confusion_matrix(y_test, y_pred)` | Aciertos/errores por clase | Tabla para LEER |
| `modelo.inertia_` (KMeans) | Qué tan "apretados" los grupos | Más bajo |
| `silhouette_score(X, etiquetas)` | Separación de grupos | Cerca de 1 |
| `modelo.coef_`, `modelo.intercept_` (regresión) | Pendiente y base | Interpretar |

```python
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, confusion_matrix
```

## 4. Escalado (KNN y K-Means: ¡obligatorio!) ⚖️

```python
from sklearn.preprocessing import StandardScaler

escalador = StandardScaler()
X_train_es = escalador.fit_transform(X_train)  # aprende + aplica (SOLO en train)
X_test_es  = escalador.transform(X_test)       # aplica la misma escala
```

> ¿Por qué? Si `gasto` llega a 1500 y `visitas` a 25, el primero aplasta al
> segundo en cualquier "distancia". Escalar lo iguala.

## 5. El truco del `fit` vs `transform` (la regla de oro)

| Función | Qué hace | ¿Cuándo? |
|---------|----------|----------|
| `.fit_transform(X)` | Aprende Y aplica | **Solo sobre entrenamiento** |
| `.transform(X)` | Aplica lo ya aprendido | Sobre prueba y datos nuevos |

> ⚠️ Si `transform` sobre el examen usa información del examen → **trampa**.
> Vectorizador, escalador y cualquier transformación: `fit` solo en train.

## 6. Gráficas rápidas (matplotlib)

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(7, 4))
plt.scatter(x, y, alpha=0.6)        # nube de puntos
plt.plot(x, y, color="orange")      # línea
plt.xlabel("..."); plt.ylabel("...")
plt.title("..."); plt.grid(alpha=0.3)
plt.savefig("mi_grafica.png", dpi=120)   # ← primero
plt.show()                               # ← después
```

## 7. Modelos que usaste semana a semana

| Semana | Modelo | Línea mágica |
|--------|--------|--------------|
| 3 | Regresión lineal | `LinearRegression().fit(X_train, y_train)` |
| 4 | Árbol de decisión | `DecisionTreeClassifier(max_depth=3, random_state=42)` |
| 5 | KNN | `KNeighborsRegressor(n_neighbors=3)` + escalado |
| 6 | K-Means | `KMeans(n_clusters=k, n_init=10, random_state=42)` |
| 7 | Red neuronal | `MLPClassifier(hidden_layer_sizes=(64,), max_iter=20, random_state=42)` |
| 8 | Naive Bayes | `MultinomialNB().fit(X_train_vec, y_train)` |

## 8. Frase mental para no olvidar

> **1)** X son las pistas, y la respuesta. **2)** Parto train/test.
> **3)** `fit` sobre train. **4)** `predict` sobre test. **5)** Mido con métrica.
> **6)** Escribo qué significa. Siempre. En ese orden.