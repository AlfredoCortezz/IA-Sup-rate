import type { Proyecto } from "@/data/proyectos";

/**
 * Tarjeta de UN proyecto.
 * Es un "componente de servidor": no usa estado, solo recibe datos (props)
 * y los muestra. Pensado para que lo personalices con tu estilo.
 *
 * 🚩 TODO (Semana 9): cambia el diseño, agrega una imagen, un botón de
 * "Ver proyecto" (usando `proyecto.enlace`), o etiquetas de colores.
 */
export function ProyectoCard({ proyecto }: { proyecto: Proyecto }) {
  return (
    <article className="card">
      <div className="card-emoji" aria-hidden>
        {proyecto.emoji}
      </div>
      <h3>{proyecto.titulo}</h3>
      <p>{proyecto.descripcion}</p>

      <div className="tags">
        {proyecto.tecnologias.map((tec) => (
          <span key={tec} className="tag">
            {tec}
          </span>
        ))}
      </div>

      <div className="card-footer">
        <span className="semana">Semana {proyecto.semana}</span>
        {proyecto.enlace && (
          <a href={proyecto.enlace} target="_blank" rel="noopener noreferrer">
            Ver proyecto →
          </a>
        )}
      </div>
    </article>
  );
}
