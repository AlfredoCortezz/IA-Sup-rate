# 🚦 Pistas — Semana 6 · K-Means (Clientes)

> Abre `semana-06/reto_kmeans.py`, mira el TODO que te atascó y baja SOLO la
> pista que necesites.

---

## TODO 1 — Limpieza

- 🚦 **1º intento:** qué columnas podrían ser ruido (que no ayudan a agrupar
  clientes parecidos) y qué columnas describen el comportamiento del cliente.
- 🚦 **2º intento:** revisa `df.isnull().sum()` y cuida que las columnas usadas
  sean numéricas.
- 🚦 **3º intento:** usa `df.describe().T` para ver rangos, y recapacita si
  necesitas escalar (cheatsheet 🐍 apartado 4) antes de pasar al clustering.

---

## TODO 2 — Elegir el número de grupos (método del codo)

- 🚦 **1º intento:** el codo se calcula entrenando K-Means con k=1, 2, 3, … y
  guardando `modelo.inertia_` (cuánta distancia hay dentro de cada grupo).
- 🚦 **2º intento:** el codo es **el punto donde el número empieza a bajar muy
  poquito** al subir k. Gráfica `k` (eje x) vs `inertia` (eje y) para verlo.
- 🚦 **3º intento:** Necesitas un bucle:
  ```python
  inertias = []
  K = range(1, 9)
  for k in K:
      km = KMeans(n_clusters=k, n_init=10, random_state=42)
      km.fit(X)
      inertias.append(km.inertia_)
  ```

📌 **"n_init=10" no es opcional:** sin él, K-Means puede caer en un mal
mínimo. Pónselo.

---

## TODO 3 — Entrenar con k elegido

- 🚦 **1º intento:** ahora sí, un solo K-Means con el k del codo.
  `modelo.fit_predict(X)` te devuelve las etiquetas de cada fila.
- 🚦 **2º intento:** `etiquetas = modelo.labels_` (¡se escribe con `labels_` con guion bajo al final!). Guárdalas en el DataFrame como columna `cluster`.
- 🚦 **3º intento:** `df["cluster"] = etiquetas` y luego
  `df.groupby("cluster").mean()` → ¡ya te da el "perfil" de cada grupo!

---

## TODO 4 — Perfil de los grupos

- 🚦 **1º intento:** la media de cada grupo `groupby(...).mean()` te dice qué
  tan joven/viejo, cuánto gasta, cuántas visitas. Dales nombre.
- 🚦 **2º intento:** une el gráfico de dispersión del archivo con colores por
  `cluster` (parámetro `c=` de `scatter`).
- 🚦 **3º intento:** ejemplo con color:
  ```python
  plt.scatter(df["edad"], df["visitas"], c=df["cluster"],
              cmap="viridis", alpha=0.7)
  ```
  ¿Qué grupo es el "joven con muchas visitas"? Etiqueta la respuesta como texto.

---

## 🔥 Reto extra (silhouette)

- 🚦 **1º intento:** `silhouette_score` está importada. Se usa sobre X y las
  etiquetas del modelo YA entrenado: `silhouette_score(X, modelo.labels_)`.
- 🚦 **2º intento:** calcúlalo para k=2..8 y gráficalo. El k con el **valor más
  alto** es el que mejor separa los grupos.
- 🚦 **3º intento:** ¿coincide con tu codo? Comenta SI coinciden y por qué
  crees que sí (o no).

---

## 🧠 Preguntas típicas del autochequeo

- **¿Qué es un centroide?** El "centro promedio" de un grupo (la media de sus
  miembros). K-Means asigna cada punto al centroide más cercano.
- **¿Silhouette cerca de 1?** Grupos muy separados y compactos (clustering
  bueno). Negativo = puntos en el grupo equivocado.
- **Variables a usar:** las que describan el comportamiento del cliente y sean
  numéricas. El "id" no, el TÍTULO no — son datos únicos, no describen grupos.