"use client";

import { useEffect, useRef, useState, type FormEvent } from "react";

/**
 * 🧠 Tutor de IA — widget flotante de ayuda.
 *
 * Corre en el NAVEGADOR ("use client") porque usa estado (mensajes, input).
 * Se conecta a /api/tutor (el endpoint de este mismo proyecto) para que
 * funcione igual en localhost y en Vercel.
 *
 * 🚩 TODO (Semana 10): puedes añadir "borrar conversación", botones de
 * voz, o guardar el historial en localStorage. La estructura de llamada
 * a la API es la misma que ya usas con los proyectos.
 */

type Burbuja = { autor: "usuario" | "tutor"; texto: string };

const SUGERENCIAS = [
  "¿Por qué separar train y test?",
  "¿Cómo escalo los datos?",
  "¿Qué es el codo de K-Means?",
  "Me da un error 2D",
  "¿Qué significa max_depth?",
];

const MENSAJE_INICIAL: Burbuja = {
  autor: "tutor",
  texto: "👋 ¡Hola! Soy tu tutora del curso. Pregúntame sobre teoría, errores o pistas de los retos (te doy pistas, ¡no la respuesta final! 😉). Empieza con una sugerencia:",
};

export function TutorChat() {
  const [abierto, setAbierto] = useState(false);
  const [mensajes, setMensajes] = useState<Burbuja[]>([MENSAJE_INICIAL]);
  const [entrada, setEntrada] = useState("");
  const [cargando, setCargando] = useState(false);
  const fondoRef = useRef<HTMLDivElement>(null);

  // Autoscroll: al llegar una burbuja nueva, bajamos hasta el final.
  useEffect(() => {
    if (fondoRef.current) {
      fondoRef.current.scrollTop = fondoRef.current.scrollHeight;
    }
  }, [mensajes, abierto]);

  async function enviar(texto: string) {
    const pregunta = texto.trim();
    if (!pregunta || cargando) return;

    setMensajes((m) => [...m, { autor: "usuario", texto: pregunta }]);
    setEntrada("");
    setCargando(true);

    try {
      const resp = await fetch("/api/tutor", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje: pregunta }),
      });

      if (!resp.ok) {
        throw new Error(`La API respondió con status ${resp.status}`);
      }

      const json = (await resp.json()) as { respuesta?: string };
      const respuesta = json.respuesta ?? "Mmm, no entendí bien. Intenta reformular la pregunta.";
      setMensajes((m) => [...m, { autor: "tutor", texto: respuesta }]);
    } catch (error) {
      setMensajes((m) => [
        ...m,
        {
          autor: "tutor",
          texto: `😵 No pude consultar al tutor: ${
            error instanceof Error ? error.message : "error de conexión"
          }. ¿Está corriendo el servidor?`,
        },
      ]);
    } finally {
      setCargando(false);
    }
  }

  function manejarEnvio(evento: FormEvent) {
    evento.preventDefault();
    void enviar(entrada);
  }

  return (
    <>
      {/* Botón flotante */}
      <button
        type="button"
        className="tutor-btn"
        aria-label="Abrir el tutor de IA"
        onClick={() => setAbierto((a) => !a)}
      >
        {abierto ? "✖️" : "🤖"}
      </button>

      {/* Panel del chat */}
      {abierto && (
        <aside className="tutor-panel" aria-label="Tutor de IA">
          <header className="tutor-cabecera">
            <strong>🤖 Tutor de IA</strong>
            <span>pistas, nunca soluciones</span>
          </header>

          <div className="tutor-mensajes" ref={fondoRef}>
            {mensajes.map((m, i) => (
              <p
                key={i}
                className={m.autor === "tutor" ? "burbuja tutor" : "burbuja usuario"}
              >
                {m.texto}
              </p>
            ))}
            {cargando && <p className="burbuja tutor escribiendo">Pensando… ✍️</p>}
          </div>

          <div className="tutor-sugerencias">
            {SUGERENCIAS.map((s) => (
              <button key={s} type="button" onClick={() => void enviar(s)}>
                {s}
              </button>
            ))}
          </div>

          <form className="tutor-input" onSubmit={manejarEnvio}>
            <input
              type="text"
              placeholder="Escribe tu pregunta..."
              value={entrada}
              onChange={(e) => setEntrada(e.target.value)}
              disabled={cargando}
              aria-label="Tu pregunta"
            />
            <button type="submit" disabled={cargando || !entrada.trim()}>
              Enviar
            </button>
          </form>
        </aside>
      )}
    </>
  );
}