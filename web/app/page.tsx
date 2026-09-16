import { ProyectosSection } from "@/components/ProyectosSection";

/**
 * ============================================================
 *  PÁGINA PRINCIPAL — TU PORTAFOLIO (Semana 9)
 * ============================================================
 *  Esta es la página que se muestra en "/" (la raíz del sitio).
 *
 *  La sección de proyectos conecta con la API simulada (Semana 10):
 *  hace un GET a /api/proyectos y muestra las tarjetas. Si además
 *  desplegamos en Vercel, ¡funciona igual en internet!
 *
 *  🚩 TODO (Semana 9): cambia todo lo marcado con "TU NOMBRE", "TU FRASE",
 *  tus redes y tus habilidades. Haz este portafolio TUYO.
 */
export default function Home() {
  const habilidades = [
    "Python",
    "scikit-learn",
    "pandas",
    "Análisis de datos",
    "HTML / CSS",
    "JavaScript",
    "Next.js",
    "TypeScript",
    "Trabajo en equipo",
  ];

  return (
    <main className="contenedor">
      {/* ---------- HERO: la primera impresión ---------- */}
      <header className="hero">
        <p className="saludo">👋 ¡Hola! Soy</p>
        {/* 🚩 TODO: escribe tu nombre */}
        <h1>TU NOMBRE AQUÍ</h1>
        {/* 🚩 TODO: escribe tu frase de presentación */}
        <p className="frase">
          Estudiante de bachillerato aprendiendo IA y desarrollo web. Aquí muestro
          todo lo que construí en 10 semanas. 🚀
        </p>
        <div className="hero-links">
          {/* 🚩 TODO: cambia los "#" por tus links reales (GitHub, email, etc.) */}
          <a href="#" className="btn">
            📂 Mi GitHub
          </a>
          <a href="#" className="btn-sec">
            ✉️ Contáctame
          </a>
        </div>
      </header>

      {/* ---------- SOBRE MÍ ---------- */}
      <section className="seccion">
        <h2>🧑‍🔬 Sobre mí</h2>
        {/* 🚩 TODO: cuéntale al mundo quién eres y qué te gusta de la IA */}
        <p>
          Empecé el curso sin saber nada de Inteligencia Artificial y terminé
          entrenando mis propios modelos: desde predecir calificaciones hasta leer
          dígitos con una red neuronal. Me interesa especialmente
          ______________________ (escribe aquí tu área favorita).
        </p>
      </section>

      {/* ---------- HABILIDADES ---------- */}
      <section className="seccion">
        <h2>🛠️ Habilidades</h2>
        <div className="tags">
          {habilidades.map((h) => (
            <span key={h} className="tag">
              {h}
            </span>
          ))}
        </div>
      </section>

      {/* ---------- PROYECTOS (conecta con la API) ---------- */}
      <section className="seccion" id="proyectos">
        <h2>📦 Mis proyectos</h2>
        <p className="subtitulo">
          Estos datos se cargan desde la API <code>/api/proyectos</code> y puedes
          agregar más con el formulario. ¡Pruébalo!
        </p>
        <ProyectosSection />
      </section>

      <footer className="footer">
        <p>
          Hecho con 💜 durante el curso de IA y Desarrollo Web ·{" "}
          {/* 🚩 TODO: tu nombre y el año */}
          <strong>TU NOMBRE</strong> · {new Date().getFullYear()}
        </p>
      </footer>
    </main>
  );
}
