"use client";

import { useEffect, useState } from "react";

/**
 * ============================================================
 *  📊 PANEL DE PROGRESO — el curso de un vistazo
 * ============================================================
 *  Muestra las 10 semanas (fases, puntaje, roles) con casillas
 *  que se guardan en localStorage del navegador: tu progreso
 *  sobrevive a recargas y a cerrar la pestaña.
 *
 *  🚩 TODO (Semana 10): conecta esto a la API (POST /api/... para
 *  guardar en el "backend") y muéstralo como una sección de tu web.
 */

type Semana = {
  numero: number;
  emoji: string;
  titulo: string;
  fase: string;
  puntos: number;
  descripcion: string;
};

const SEMANAS: Semana[] = [
  { numero: 1, emoji: "🕵️", titulo: "¿Qué es la IA de verdad?", fase: "Fundamentos", puntos: 10, descripcion: "Cazador(a) de mitos + cuestionario en index.html." },
  { numero: 2, emoji: "⚡", titulo: "IA Generativa: tu copiloto", fase: "Fundamentos", puntos: 10, descripcion: "Prompt Battle en dashboard-semana2.html." },
  { numero: 3, emoji: "📈", titulo: "Regresión Lineal", fase: "Machine Learning", puntos: 20, descripcion: "Predecir tu nota con horas de estudio." },
  { numero: 4, emoji: "🚢", titulo: "Árbol de Decisión (Titanic)", fase: "Machine Learning", puntos: 25, descripcion: "Interpretar decisiones + sobreajuste." },
  { numero: 5, emoji: "🎬", titulo: "KNN: recomendador", fase: "Machine Learning", puntos: 20, descripcion: "Escalar, distancias y k vecinos." },
  { numero: 6, emoji: "🛍️", titulo: "K-Means: clientes", fase: "Machine Learning", puntos: 20, descripcion: "Clustering sin supervisión + método del codo." },
  { numero: 7, emoji: "🔢", titulo: "Redes Neuronales (MNIST)", fase: "IA profunda", puntos: 25, descripcion: "Leer dígitos con MLPClassifier." },
  { numero: 8, emoji: "💬", titulo: "NLP: sentimiento", fase: "IA profunda", puntos: 20, descripcion: "Tfidf + Naive Bayes sobre reseñas." },
  { numero: 9, emoji: "🖥️", titulo: "Tu portafolio con Next.js", fase: "Desarrollo Web", puntos: 25, descripcion: "Componentes, TypeScript y tu página." },
  { numero: 10, emoji: "🚀", titulo: "API + despliegue en Vercel", fase: "Desarrollo Web", puntos: 25, descripcion: "Conectar la API y publicar tu link." },
];

const ROLES = [
  { emoji: "👑", rol: "Capitán / Integrador", tarea: "organiza, junta las piezas y sube el reto a GitHub" },
  { emoji: "🔍", rol: "Investigador(a)", tarea: "busca teoría, documenta y cita fuentes" },
  { emoji: "💻", rol: "Código / Datos", tarea: "escribe el código, limpia datos y prueba" },
  { emoji: "🎤", rol: "Presentador(a)", tarea: "prepara la explicación y defiende el reto" },
];

const TOTAL_PUNTOS = SEMANAS.reduce((acc, s) => acc + s.puntos, 0);
const CLAVE = "ia-sup-rate-progreso";

export default function ProgresoPage() {
  const [hechas, setHechas] = useState<Record<number, boolean>>({});
  const [listo, setListo] = useState(false);

  // Cargar desde localStorage SOLO al montar (evita saltos de hidratación).
  useEffect(() => {
    try {
      const guardado = localStorage.getItem(CLAVE);
      if (guardado) setHechas(JSON.parse(guardado) as Record<number, boolean>);
    } catch {
      // localStorage dañado o no disponible: empezamos de cero.
    } finally {
      setListo(true);
    }
  }, []);

  function alternar(numero: number) {
    setHechas((prev) => {
      const siguiente = { ...prev, [numero]: !prev[numero] };
      try {
        localStorage.setItem(CLAVE, JSON.stringify(siguiente));
      } catch {
        // Sin almacenamiento: el progreso se pierde al recargar.
      }
      return siguiente;
    });
  }

  function reiniciar() {
    setHechas({});
    try {
      localStorage.removeItem(CLAVE);
    } catch {
      // nada que hacer
    }
  }

  const totalHechas = SEMANAS.filter((s) => hechas[s.numero]).length;
  const puntosConseguidos = SEMANAS.reduce(
    (acc, s) => acc + (hechas[s.numero] ? s.puntos : 0),
    0,
  );
  const porcentaje = Math.round((totalHechas / SEMANAS.length) * 100);

  return (
    <main className="contenedor">
      <header className="hero">
        <p className="saludo">🎯 Mi progreso en el curso</p>
        <h1>IA Sup-rate · 10 semanas</h1>
        <p className="frase">
          Marca cada reto cuando lo termines. Tu progreso se guarda en este
          navegador. Los roles se rotan: mínimo 1 vez cada quien en las 10
          semanas.
        </p>

        {/* Barra de progreso */}
        <div className="progreso-contenedor" aria-label={`${porcentaje}% completado`}>
          <div
            className="progreso-barra"
            style={{ width: listo ? `${porcentaje}%` : "0%" }}
          />
        </div>
        <p className="progreso-texto">
          ✅ {totalHechas}/10 semanas · {puntosConseguidos}/{TOTAL_PUNTOS} pts ·{" "}
          {porcentaje}%
        </p>
      </header>

      <section className="seccion">
        <h2>🗓️ Plan de las 10 semanas</h2>
        {SEMANAS.map((s) => {
          const hecho = !!hechas[s.numero];
          return (
            <article key={s.numero} className={`semana-fila ${hecho ? "hecho" : ""}`}>
              <button
                type="button"
                className="semana-check"
                aria-label={`${hecho ? "Desmarcar" : "Marcar"} semana ${s.numero}`}
                onClick={() => alternar(s.numero)}
              >
                {hecho ? "✅" : "⬜"}
              </button>
              <div className="semana-info">
                <h3>
                  {s.emoji} Semana {s.numero} — {s.titulo}
                </h3>
                <p className="semana-detalles">
                  {s.descripcion}{" "}
                  <span className="semana-puntos">
                    {hecho ? `+${s.puntos} pts` : `${s.puntos} pts`}
                  </span>
                </p>
              </div>
              <span className="semana-fase">{s.fase}</span>
            </article>
          );
        })}
      </section>

      <section className="seccion">
        <h2>👥 Roles del equipo</h2>
        <div className="tags">
          {ROLES.map((r) => (
            <span key={r.rol} className="tag" title={r.tarea}>
              {r.emoji} {r.rol}
            </span>
          ))}
        </div>
        <p className="subtitulo">
          Rotad al menos una vez en las 10 semanas: que nadie se quede siempre
          con el mismo rol.
        </p>
      </section>

      {totalHechas > 0 && (
        <button type="button" className="btn-sec" onClick={reiniciar}>
          ♻️ Reiniciar mi progreso
        </button>
      )}
    </main>
  );
}