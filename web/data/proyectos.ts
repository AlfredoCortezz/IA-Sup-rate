/**
 * ============================================================
 *  TUS PROYECTOS — edita este archivo con tus datos reales
 * ============================================================
 *  Cada objeto de la lista es UN proyecto de tu portafolio.
 *  🚩 TODO (Semana 9): cambia estos ejemplos por tus trabajos de las
 *  semanas 3 a 8 (tu modelo del Titanic, tu red neuronal, etc.).
 *
 *  `id` debe ser único. `semana` indica de qué reto del curso viene.
 */

export type Proyecto = {
  id: number;
  titulo: string;
  descripcion: string;
  tecnologias: string[];
  emoji: string;
  enlace?: string;
  semana: number;
};

export const proyectosIniciales: Proyecto[] = [
  {
    id: 1,
    titulo: "Cazadores de Mitos",
    descripcion:
      "Cuestionario interactivo sobre mitos y realidades de la IA. Mi primer contacto con el tema.",
    tecnologias: ["HTML", "CSS", "JavaScript"],
    emoji: "🧠",
    semana: 1,
  },
  {
    id: 2,
    titulo: "Prompt Battle Dashboard",
    descripcion:
      "Dashboard con evaluación teórica y generador automático de retos de ingeniería de prompts.",
    tecnologias: ["HTML", "CSS", "JavaScript"],
    emoji: "✍️",
    semana: 2,
  },
  {
    id: 3,
    titulo: "Predictor de calificaciones",
    descripcion:
      "Modelo de regresión lineal que estima la nota según las horas de estudio.",
    tecnologias: ["Python", "scikit-learn", "pandas"],
    emoji: "📈",
    semana: 3,
  },
  {
    id: 4,
    titulo: "Árbol del Titanic",
    descripcion:
      "Árbol de decisión que predice la supervivencia de los pasajeros del Titanic.",
    tecnologias: ["Python", "scikit-learn", "seaborn"],
    emoji: "🚢",
    semana: 4,
  },
  {
    id: 5,
    titulo: "Recomendador de películas",
    descripcion: "Sistema KNN que sugiere películas parecidas a tus favoritas.",
    tecnologias: ["Python", "scikit-learn"],
    emoji: "🎬",
    semana: 5,
  },
  {
    id: 6,
    titulo: "Segmentador de clientes",
    descripcion: "Clustering K-Means para descubrir tipos de clientes en datos de negocio.",
    tecnologias: ["Python", "scikit-learn", "matplotlib"],
    emoji: "🛒",
    semana: 6,
  },
  {
    id: 7,
    titulo: "Red neuronal lectora de dígitos",
    descripcion: "Red neuronal que reconoce números escritos a mano (MNIST).",
    tecnologias: ["Python", "scikit-learn"],
    emoji: "🔢",
    semana: 7,
  },
  {
    id: 8,
    titulo: "Analizador de sentimiento",
    descripcion: "NLP que clasifica reseñas como positivas o negativas.",
    tecnologias: ["Python", "scikit-learn", "NLP"],
    emoji: "💬",
    semana: 8,
  },
];
