# 🚦 Pistas — Semana 7 · Redes Neuronales (MNIST)

> Abre `semana-07/reto_mnist.py`, mira el TODO que te atascó y baja SOLO la
> pista que necesites.

---

## TODO 1 — Cargar los datos

- 🚦 **1º intento:** dos opciones cargadas al inicio: los dígitos pequeños
  (`load_digits()`) y MNIST grande (`fetch_openml`). Si tu PC lo aguanta, usa
  MNIST: es el look real de "moda en ML".
- 🚦 **2º intento:** los datos vienen como un DataFrame/list-one. Imprime
  `X.shape` y `y.shape` ANTES de tocar nada y piensa qué significa cada número.
- 🚦 **3º intento:** una imagen 28×28 se aplana a **784 números**: cada píxel es
  una "entrada" a la red. Eso es "por qué 784".

---

## TODO 2 — Entender qué hace una neurona

- 🚦 **1º intento:** antes de programar explica EN TUS PALABRAS (una frase en un
  print o comentario) qué es una neurona: multiplica entradas × pesos, los suma
  y aplica una activación.
- 🚦 **2º intento:** no hace falta fórmula mágica: "cada llegada tiene un peso;
  la neurona suma (entrada × peso) y decide si se activa".
- 🚦 **3º intento:** usa esa frase como tu respuesta. Es la teoría que te van a
  preguntar.

---

## TODO 3 — Escalar (normalizar píxeles)

- 🚦 **1º intento:** los píxeles van de 0 a 255. Partirlos entre 255 los deja en
  0–1, y las redes se entrenan mejor con valores pequeños y parejos.
- 🚦 **2º intento:** divide por el máximo posible (255), no por un valor tuyo
  que se te ocurra pirata dejar.
- 🚦 **3º intento:** `X = X / 255.0`. Listo.

> ⚠️ ¿Recuerdas la **regla de oro** del cheatsheet? Divide por 255 antes de
> cortar train/test para que la escala sea la misma en ambos.

---

## TODO 4 — Separar en entrenamiento y prueba

- 🚦 **1º intento:** `train_test_split` con `test_size` ~0.2.
- 🚦 **2º intento:** ¿qué pasa si usas `stratify=y`? Mira la distribución de
  dígitos con y sin stratify en un `value_counts`... 
- 🚦 **3º intento:** `stratify=y` reparte la MISMA proporción de cada dígito en
  train y en test. El autochequeo te preguntará qué hace. ¡Dilo!

---

## TODO 5 — Entrenar la red

- 🚦 **1º intento:** `MLPClassifier` ya está importado. Su superpoder es
  `hidden_layer_sizes` (cuántas neuronas y capas escondidas).
- 🚦 **2º intento:** empieza pequeñito: `MLPClassifier(hidden_layer_sizes=(64,),
  max_iter=20, random_state=42)` → fit con X_train.
- 🚦 **3º intento:** si tarda mucho, baja `max_iter`; si no llega a aprender,
  súbelo. `(64,)` = una capa de 64 neuronas; `(128, 64)` = dos capas.

📌 Contesta cómo cambia el acc con distintos `hidden_layer_sizes` → eso es el
reto extra.

---

## 🔬 Reto extra (arquitecturas)

- 🚦 **1º intento:** compara 3 redes: una pequeña `(64,)`, una mediana `(128,
  64)`, una grande `(256, 128, 64)`.
- 🚦 **2º intento:** cada una: entrenar, `predict`, `accuracy_score`. Fíjate que
  la grande tarda MUCHO más y que el acc sube cada vez menos (rendimientos
  decrecientes).
- 🚦 **3º intento:** responde: ¿merece la pena la grande? ¿Dónde está el punto
  dulce? Leerás "accuracy ~93 %, 95 %, 95.5 %... y 3 veces más tiempo".

---

## 🧠 Preguntas típicas del autochequeo

- **¿Por qué 784 entradas?** = 28×28 píxeles de cada imagen.
- **¿Qué es "escondida"?** La capa entre la entrada y la salida; aprende
  patrones intermedios (cómo se hace). No ves sus activaciones directamente.
- **¿Qué hace `hidden_layer_sizes=(64,)`?** Una capa oculta con 64 neuronas.
- **¿Por qué normalizar a 0–1?** Redes entrenan más estable con valores
  pequeños y parejos (evita pesos gigantes).

> 💡 Si la primera vez tarda, es porque MNIST completo es grande. Usa
> `max_iter=20` para el primer intento.