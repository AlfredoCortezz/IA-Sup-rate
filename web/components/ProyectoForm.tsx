"use client";

import { useState } from "react";
import { crearProyecto, type NuevoProyecto } from "@/lib/api";

/**
 * Formulario para crear un proyecto (envía un POST a la API).
 *
 * "use client" arriba significa: este componente corre en el NAVEGADOR,
 * por eso puede usar useState y eventos como onSubmit.
 *
 * 🚩 TODO (Semana 10): agrega validación (título obligatorio, mínimo de
 * caracteres), campos nuevos (link, imagen) y mensajes de error claros.
 */
export function ProyectoForm({ onCreado }: { onCreado: () => void }) {
  const [titulo, setTitulo] = useState("");
  const [descripcion, setDescripcion] = useState("");
  const [tecnologias, setTecnologias] = useState("");
  const [emoji, setEmoji] = useState("🚀");
  const [enviando, setEnviando] = useState(false);
  const [mensaje, setMensaje] = useState<string | null>(null);

  async function manejarEnvio(evento: React.FormEvent) {
    evento.preventDefault();

    // 🚩 TODO: valida aquí antes de enviar (por ejemplo, que el título no esté vacío).
    if (!titulo.trim() || !descripcion.trim()) {
      setMensaje("El título y la descripción son obligatorios.");
      return;
    }

    const nuevo: NuevoProyecto = {
      titulo: titulo.trim(),
      descripcion: descripcion.trim(),
      tecnologias: tecnologias
        .split(",")
        .map((t) => t.trim())
        .filter(Boolean),
      emoji: emoji || "🚀",
      semana: 10,
    };

    try {
      setEnviando(true);
      setMensaje(null);
      await crearProyecto(nuevo);
      setTitulo("");
      setDescripcion("");
      setTecnologias("");
      setEmoji("🚀");
      setMensaje("¡Proyecto agregado! 🎉");
      onCreado();
    } catch (error) {
      setMensaje(error instanceof Error ? error.message : "Error al crear el proyecto");
    } finally {
      setEnviando(false);
    }
  }

  return (
    <form className="form" onSubmit={manejarEnvio}>
      <h3>➕ Agregar un proyecto</h3>

      <div className="form-fila">
        <input
          type="text"
          placeholder="Emoji (ej. 🤖)"
          value={emoji}
          onChange={(e) => setEmoji(e.target.value)}
          maxLength={2}
          aria-label="Emoji"
        />
        <input
          type="text"
          placeholder="Título del proyecto"
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
        />
      </div>

      <textarea
        placeholder="Descripción breve..."
        value={descripcion}
        onChange={(e) => setDescripcion(e.target.value)}
      />

      <input
        type="text"
        placeholder="Tecnologías separadas por coma (Python, Next.js...)"
        value={tecnologias}
        onChange={(e) => setTecnologias(e.target.value)}
      />

      <button type="submit" disabled={enviando}>
        {enviando ? "Enviando..." : "Publicar proyecto"}
      </button>

      {mensaje && <p className="form-mensaje">{mensaje}</p>}
    </form>
  );
}
