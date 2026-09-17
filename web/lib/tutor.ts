/**
 * ============================================================
 *  "TUTOR DE IA" — base de conocimiento del curso (Semanas 3–8)
 * ============================================================
 *  Este módulo es un tutor SIN necesidad de API externa: responde con
 *  reglas y pistas del curso, nunca con la respuesta final de un reto.
 *
 *  🚩 TODO (Semana 10): puedes conectarlo a un modelo real (OpenAI, Groq...)
 *  pasándole este corpus como contexto. La función `buscarRespuesta` es
 *  la que tendrías que sustituir por la llamada al modelo.
 */

/** Una entrada del banco de conocimiento. */
type Entrada = {
  /** Palabras clave (ya normalizadas: minúsculas y sin tildes). */
  palabras: string[];
  /** Respuesta que se muestra (pistas, nunca la solución final). */
  respuesta: string;
  /** Número mínimo de palabras clave que deben aparecer (default 1). */
  minimo?: number;
};

const SALUDO = "👋 ¡Hola! Soy tu tutora del curso de IA. Pregúntame sobre los retos, errores o teoría (Semanas 3–10). Recuerda la regla de oro: te doy PISTAS, no la respuesta final. 😉";

const FALLBACK =
  "🤔 No reconozco eso todavía. Prueba a preguntarme cosas como:\n\n" +
  "• \"¿por qué separar train y test?\"\n" +
  "• \"¿cómo escalo los datos?\"\n" +
  "• \"¿qué es el codo de K-Means?\"\n" +
  "• \"me da un error 2D\"\n" +
  "• \"¿qué significa max_depth?\"\n\n" +
  "Puedes preguntar por \"pista semana 6\" y te digo dónde están las pistas completas 📍";

/** Normaliza texto: minúsculas, sin tildes ni puntuación extra. */
function normalizar(texto: string): string {
  return texto
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^\p{L}\p{N}\s]/gu, " ");
}

const ENTRADAS: Entrada[] = [
  // ---------- SALUDOS / DESPEDIDAS ----------
  {
    palabras: ["hola", "buenas", "buenos dias", "buenas tardes", "hey", "holi", "que tal"],
    minimo: 1,
    respuesta: SALUDO,
  },
  {
    palabras: ["gracias", "te agradezco", "muchas gracias", "thx"],
    minimo: 1,
    respuesta: "¡De nada! 💪 Y recuerda: la mejor manera de aprender es explicarlo con tus palabras. Cuando lo logres, ¡cuéntaselo a tu equipo!",
  },
  {
    palabras: ["adios", "hasta luego", "nos vemos", "chao"],
    minimo: 1,
    respuesta: "¡Hasta pronto! 👋 Aquí estaré cuando necesites una pista.",
  },

  // ---------- LA REGLA DE ORO (train/test, fit/transform) ----------
  {
    palabras: ["regla de oro", "hacer trampa", "haciendo trampa", "examen", "mirar las respuestas"],
    minimo: 1,
    respuesta:
      "La REGLA DE ORO del curso: lo que aprende el modelo NO puede ver la respuesta del examen.\n\n" +
      "Concretamente: `fit_transform` solo se hace sobre el entrenamiento (train) y sobre la prueba (test) solo `transform` o `predict`.\n\n" +
      "Si el vectorizador, el escalador o el modelo 'ven' test para aprender, estás midiendo con trampa y las métricas mienten. 📍 Ver `tools/cheatsheets/02-python-ml.md`.",
  },
  {
    palabras: ["fit transform", "transform", "fit_transform", "escalador", "vectorizador", "transformar", "normalizar", "normalizo", "normaliz"],
    minimo: 1,
    respuesta:
      "Diferencia clave:\n\n" +
      "• `fit_transform(X_train)` → el modelo APRENDE la transformación y la aplica. Se usa UNA vez, solo sobre train.\n" +
      "• `transform(X_test)` → aplica la transformación YA aprendida a datos nuevos (test).\n\n" +
      "⚠️ Si haces `fit_transform(X_test)` 'estás viendo el examen'. Es la Regla de Oro de la semana (Semana 4/escalado y Semana 8/vectorizador).",
  },

  // ---------- TRAIN/TEST ----------
  {
    palabras: ["train", "test", "separar", "partir", "entrenamiento", "prueba", "train_test_split", "test_size", "random_state", "stratify", "destinar"],
    minimo: 1,
    respuesta:
      "🧠 ¿Por qué separar train y test?\n\n" +
      "El train es 'los ejercicios de clase' y el test es 'el examen con preguntas NUEVAS'. Si evaluaras al modelo con los mismos datos que entrenó, sacaría un 100 % porque se los 'memorizó'.\n\n" +
      "`test_size=0.2` → 80 % para entrenar, 20 % para el examen.\n" +
      "`random_state=42` → mismo reparto siempre (para que sea justo comparar).\n" +
      "`stratify=y` → reparte la misma proporción de cada clase/pregunta en el examen. 📍 Cheatsheet 🐍 apartado 2.",
  },

  // ---------- ERRORES COMUNES ----------
  {
    palabras: ["2d", "1d", "valueerror", "expected 2d", "serie", "tabla", "got 1d array", "array 1"],
    minimo: 1,
    respuesta:
      "¡Ese error (`Expected 2D array, got 1D array`) es de los más comunes del curso!\n\n" +
      "scikit-learn espera que X sea una TABLA (2D: filas × columnas). Si hiciste `X = df[\"horas\"]` obtienes una SERIE (1D).\n\n" +
      "Arreglo: el doble corchete → `X = df[[\"horas\"]]`.\n" +
      "Memoria: serie = 1D (una columna), tabla = 2D (para el modelo). 📍 tools/06-errores-comunes.md nº1.",
  },
  {
    palabras: ["nan", "null", "faltan", "huecos", "vacios", "vacío", "dropna", "fillna", "infinity", "isnull", "no aplica"],
    minimo: 1,
    respuesta:
      "Valores NaN/Null = celdas vacías. Los modelos no saben qué hacer con ellas (muchas veces dan error `Input contains NaN`).\n\n" +
      "Plan: revisa `df.isnull().sum()`, luego rellena con la mediana de su columna `df[\"col\"].fillna(df[\"col\"].median())` o borra filas con `df.dropna()`. 📍 Errores comunes nº4 y nº6.",
  },
  {
    palabras: ["keyerror", "no existe la columna", "columna", "columns", "df[", "column"],
    minimo: 1,
    respuesta:
      "`KeyError` = la columna que nombras NO existe (¿mayúsculas? ¿nombre cambiado?).\n\n" +
      "Arreglo: ejecuta `print(df.columns)` y copia el nombre EXACTO que aparezca. 📍 Errores comunes nº3.",
  },
  {
    palabras: ["nameerror", "not defined", "sin definir", "pandas", "import"],
    minimo: 1,
    respuesta:
      "`NameError: name '...' is not defined` = usas algo sin importarlo.\n\n" +
      "Recuerda `import pandas as pd`: luego escribes `pd.` (el alias), no `pandas`. Si importaste `pd` pero escribiste `pandas`, cambia por `pd`. 📍 Errores comunes nº2.",
  },
  {
    palabras: ["modulenotfound", "no module", "seaborn", "instalar", "pip install", "sklearn no", "importar libreria"],
    minimo: 1,
    respuesta:
      "`ModuleNotFoundError` = falta esa librería en tu entorno.\n\n" +
      "En Google Colab ya vienen instaladas. En tu PC (semanas 3–8) ejecuta en la terminal:\n\n" +
      "`pip install numpy pandas matplotlib scikit-learn seaborn`\n\n" +
      "Luego cierra y vuelve a abrir la terminal. 📍 Errores comunes nº9.",
  },

  // ---------- GIT ----------
  {
    palabras: ["git", "commit", "push", "pull", "rama", "branch", "github", "clone", "merge", "rebase", "status", "add"],
    minimo: 1,
    respuesta:
      "Git en resumen:\n\n" +
      "1) `git add nombres` → prepara archivos.\n" +
      "2) `git commit -m \"mensaje\"` → guarda la foto.\n" +
      "3) `git push origin tu-rama` → sube la foto a GitHub.\n\n" +
      "Si el push falla por 'non-fast-forward': `git pull --rebase origin tu-rama` y vuelve a `push`.\n" +
      "📍 tools/cheatsheets/01-git.md lo tiene todo en una página.",
  },

  // ---------- REGRESION LINEAL (S3) ----------
  {
    palabras: ["regresion", "lineal", "pendiente", "intercepto", "coef", "regresionlineal", "linearregression", "predecir calificacion", "nota", "estudio"],
    minimo: 1,
    respuesta:
      "Regresión lineal = trazas la 'recta que mejor pasa por en medio' de los datos.\n\n" +
      "• `modelo.coef_` (la pendiente) → cuánto sube la nota por cada hora extra de estudio.\n" +
      "• `modelo.intercept_` (la ordenada) → la nota base con 0 horas.\n" +
      "• MAE mide el error en puntos; R² mide qué % de la variación explica tu recta.\n\n" +
      "Pregunta típica: '¿qué significa el intercepto?' → es la nota cuando la pendiente no aporta nada. 📍 Escribe esa interpretación en tu ENTREGA.md.",
  },

  // ---------- ARBOL DE DECISION (S4) ----------
  {
    palabras: ["arbol", "decision", "titanic", "sobrevive", "pasajero", "max_depth", "max depth", "decisiontree", "profundidad", "plot_tree", "nodo", "raiz", "hoja"],
    minimo: 1,
    respuesta:
      "Árbol = el juego de las 20 preguntas convertido en IA. Cada 'nodo' pregunta algo y cada 'hoja' es la respuesta final.\n\n" +
      "• La RAÍZ es la primera pregunta (la que mejor separa, en Titanic suele ser 'sex').\n" +
      "• `max_depth=3` → solo 3 preguntas (menos sobreajuste).\n" +
      "• Pregunta clave: si `max_depth=20`, el train llega a 90-100 % pero el test se queda bajo → SOBREAJUSTE (se sabe la respuesta de memoria).\n\n" +
      "📍 tools/pistas/semana-04.md para el experimento de profundidad.",
  },
  {
    palabras: ["sobreajuste", "overfitting", "memoriza", "saba de memoria", "se sabe de memoria", "de memoria"],
    minimo: 1,
    respuesta:
      "Sobreajuste (overfitting) = el modelo se MEMORIZA el train en vez de aprender la idea general.\n\n" +
      "Cómo detectarlo: el accuracy en train está por las nubes (90-100 %) pero el de test no sube o baja.\n\n" +
      "Antídoto: limitar al modelo — para árboles `max_depth` (3-5 suele bastar), en KNN elegir k no muy pequeño, y en redes no exagerar con las capas. 📍 tools/pistas/semana-04.md y semana-07.md.",
  },

  // ---------- KNN (S5) ----------
  {
    palabras: ["knn", "vecino", "vecinos", "n_neighbors", "k vecinos", "n-neighbors", "recomend", "escalar", "escalado", "escalo", "escala", "escal", "normaliz", "standardscaler", "distancia"],
    minimo: 1,
    respuesta:
      "KNN = mira las K 'películas más parecidas' (vecinos) y copia lo que valen.\n\n" +
      "• `n_neighbors=k` → cuántos vecinos consulta. k pequeñito es nervioso (memoriza ruido); k grande promedia demasiado con todo el mundo.\n" +
      "• ANTES de KNN: ESCALA con `StandardScaler`. Si una columna va de 0 a 10 y otra de 1990 a 2020, la de años domina la 'distancia' y hace trampa.\n\n" +
      "Motivo para no usar el título de película como feature: es texto ÚNICO por fila, no sirve para generalizar. 📍 tools/pistas/semana-05.md.",
  },

  // ---------- K-MEANS (S6) ----------
  {
    palabras: ["kmeans", "k-means", "k means", "clustering", "cluster", "agrupar", "grupos", "centroide", "codo", "inertia", "elbow", "silhouette", "labels", "etiquetas", "no supervisado"],
    minimo: 1,
    respuesta:
      "K-Means agrupa puntos parecidos alrededor de centroides. Es aprendizaje NO supervisado (no hay respuestas correctas).\n\n" +
      "• Centroide = el 'centro promedio' de su grupo.\n" +
      "• Método del codo: entrena para k=1..8 y guarda `km.inertia_` (qué tan 'apretados' los grupos). El CODO es donde la curva deja de bajar rápido.\n" +
      "• `silhouette_score(X, km.labels_)` cerca de 1 = grupos bien separados.\n" +
      "• Recuerda `n_init=10` y después `km.labels_` (¡con guion bajo final!) para etiquetar cada fila. 📍 tools/pistas/semana-06.md.",
  },

  // ---------- RED NEURONAL (S7) ----------
  {
    palabras: ["mnist", "red", "neuronal", "neurona", "mlp", "mlpclassifier", "capa", "hidden", "784", "digito", "dígito", "activacion", "pesos", "neural"], 
    minimo: 1,
    respuesta:
      "Red neuronal = equipo de neuronas en capas que multiplican entradas por pesos, suman y activan.\n\n" +
      "• 784 entradas = 28×28 píxeles por imagen.\n" +
      "• Normaliza píxeles a 0–1 (`X / 255.0`) para que el entrenamiento sea estable.\n" +
      "• `MLPClassifier(hidden_layer_sizes=(64,), max_iter=20, random_state=42)`\n" +
      "  → `(64,)` = una capa oculta de 64 neuronas. Más capas = más lento y no siempre mejor.\n" +
      "• `stratify=y` reparte la MISMA proporción de cada dígito en train y test.\n\n" +
      "📍 tools/pistas/semana-07.md para el experimento de arquitecturas.",
  },

  // ---------- NLP (S8) ----------
  {
    palabras: ["nlp", "texto", "resena", "reseña", "sarcasmo", "sentimiento", "positiva", "negativa", "naive", "bayes", "multinomial", "vectorizador", "tfidf", "countvectorizer", "palabras", "token"],
    minimo: 1,
    respuesta:
      "NLP = convertir texto en números para que la máquina lo entienda.\n\n" +
      "• `CountVectorizer` cuenta cuántas veces aparece cada palabra.\n" +
      "• `TfidfVectorizer` cuenta PERO le resta peso a palabras que aparecen en todos lados ('de', 'la', 'que').\n" +
      "• `MultinomialNB` decide si la reseña es positiva o negativa con esas frecuencias.\n" +
      "• Regla de oro: `fit_transform` SOLO sobre train; al examen `transform`.\n" +
      "• Por qué falla con SARCASMO: no ve el tono de voz, solo las palabras. 'Qué maravilla… se rompió a la primera' puede sonarle positivo. 📍 tools/pistas/semana-08.md.",
  },

  // ---------- MÉTRICAS ----------
  {
    palabras: ["mae", "r2", "accuracy", "confusion", "matriz de confusion", "metrica", "metricas", "error", "f1", "precision", "recall", "score"],
    minimo: 1,
    respuesta:
      "Métricas del curso:\n\n" +
      "• `mean_absolute_error` → error medio en las unidades (notas, meses, etc.). Menos = mejor.\n" +
      "• `r2_score` → % de variación explicada. Cerca de 1 = buenísimo.\n" +
      "• `accuracy_score` → % de aciertos en clasificación.\n" +
      "• `confusion_matrix` → tabla de aciertos/errores por clase (¡la diagonal son aciertos!).\n\n" +
      "Escribe SIEMPRE qué significa en español. Ej.: 'MAE de 3.5 → el modelo se equivoca ~3.5 puntos en promedio'. 📍 Cheatsheet 🐍 apartado 3.",
  },

  // ---------- NEXT.JS / WEB (S9-10) ----------
  {
    palabras: ["next", "npm", "node", "componente", "props", "use client", "usestate", "tsx", "typescript", "vercel", "deploy", "route", "api", "fetch", "localhost", "build"],
    minimo: 1,
    respuesta:
      "Dudas de la parte web (Semanas 9-10), en resumen:\n\n" +
      "• `npm install` la primera vez; `npm run dev` para verlo en localhost:3000.\n" +
      "• Componente = una función que devuelve HTML/JSX. `Props` = los datos que entran por parámetros.\n" +
      "• Con `\"use client\"` en la primera línea puedes usar `useState`, `onClick`, etc.\n" +
      "• `route.ts` en `app/api/...` = un endpoint (GET/POST). El frontend lo llama con `fetch`.\n" +
      "• Vercel: sube el repo a GitHub, impórtalo en vercel.com y listo, link público gratis.\n\n" +
      "📍 tools/cheatsheets/03-nextjs.md y tools/04-nextjs-y-vercel.md.",
  },
  {
    palabras: ["no se reconoce", "not recognized", "enoent", "unknown command", "cannot find module", "can't resolve", "module not found", "npm is not", "error de types", "type error", "strict"],
    minimo: 1,
    respuesta:
      "Esos son errores típicos de la parte web:\n\n" +
      "• `'npm' is not recognized` → instala Node.js LTS y REABRE la terminal.\n" +
      "• `ENOENT` / `cannot find module` → te faltó `npm install` o estás en la carpeta equivocada (debe estar en `web/`).\n" +
      "• `Can't resolve '...'` → la ruta de tu import no existe (revisa mayúsculas y que el archivo esté creado).\n" +
      "• `Type 'X | undefined' is not assignable...` → TypeScript te avisa de que algo puede ser `undefined`: usa `?? \"valor por defecto\"`.\n\n" +
      "📍 tools/06-errores-comunes.md apartado 'Next.js'. El `npm run typecheck` te dice qué falla.",
  },
];

/** Busca la mejor respuesta para un mensaje. */
export function buscarRespuesta(mensaje: string): string {
  const m = normalizar(mensaje);
  if (!m) return FALLBACK;

  // Atajo: petición de pista por semana.
  const pistaSemana = m.match(/pista[s]?[ ·_-]*semana[ ·_-]*(\d)/);
  if (pistaSemana) {
    const n = pistaSemana[1];
    const archivo = n.length === 1 ? `0${n}` : n;
    return `📍 Las pistas de la **Semana ${n}** están en \`tools/pistas/semana-${archivo}.md\`.\n\nRecuerda: van de lo más sutil a casi-mostrarte-el-camino. Baja solo lo que necesites. ¡Tú puedes! 💪`;
  }

  let mejor: Entrada | null = null;
  let mejoresAciertos = 0;

  for (const e of ENTRADAS) {
    let aciertos = 0;
    for (const p of e.palabras) {
      if (m.includes(p)) aciertos++;
    }
    const minimo = e.minimo ?? 1;
    if (aciertos >= minimo && aciertos > mejoresAciertos) {
      mejor = e;
      mejoresAciertos = aciertos;
    }
  }

  return mejor ? mejor.respuesta : FALLBACK;
}