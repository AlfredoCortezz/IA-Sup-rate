"use client";

import { useCallback, useEffect, useState } from "react";
import type { Proyecto } from "@/data/proyectos";
import { getProyectos } from "@/lib/api";
import { ProyectoCard } from "./ProyectoCard";
import { ProyectoForm } from "./ProyectoForm";

/**
 * Sección que junta la LISTA (GET) y el FORMULARIO (POST).
 *
 * Este es el patrón típico de una app con API:
 *   1. Al montar, pedimos los datos (useEffect).
 *   2. Mientras llegan, mostramos "Cargando...".
 *   3. Si falla, mostramos el error y un botón de reintentar.
 *   4. Si el usuario crea algo, recargamos la lista.
 *
 * 🚩 TODO (Semana 10): agrega ordenar/filtrar por tecnología, mostrar un
 * contador de proyectos, o un botón de eliminar (método DELETE).
 */
export function ProyectosSection() {
  const [proyectos, setProyectos] = useState<Proyecto[]>([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const cargar = useCallback(async () => {
    setCargando(true);
    setError(null);
    try {
      const datos = await getProyectos();
      setProyectos(datos);
    } catch (e) {
      setError(e instanceof Error ? e.message : "No se pudo conectar con la API");
    } finally {
      setCargando(false);
    }
  }, []);

  useEffect(() => {
    cargar();
  }, [cargar]);

  return (
    <div className="proyectos-layout">
      <div className="proyectos-panel">
        <div className="proyectos-header">
          <h3>Proyectos ({proyectos.length})</h3>
          <button className="btn-sec" onClick={cargar} disabled={cargando}>
            🔄 Recargar
          </button>
        </div>

        {cargando && <p className="estado">Cargando proyectos desde la API...</p>}

        {error && (
          <div className="estado error">
            <p>😵 {error}</p>
            <button onClick={cargar}>Reintentar</button>
          </div>
        )}

        {!cargando && !error && (
          <div className="grid">
            {proyectos.map((p) => (
              <ProyectoCard key={p.id} proyecto={p} />
            ))}
          </div>
        )}
      </div>

      <ProyectoForm onCreado={cargar} />
    </div>
  );
}
