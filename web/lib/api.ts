/**
 * ============================================================
 *  CLIENTE DE API — así habla el frontend con un backend
 * ============================================================
 *  Por defecto hablamos con NUESTRA propia API simulada, la que vive en
 *  `app/api/proyectos/route.ts` (mismo dominio → funciona en Vercel).
 *
 *  Si algún día quieres apuntar a un backend REAL:
 *    - NestJS  → variable de entorno  NEXT_PUBLIC_API_URL=http://localhost:3001
 *    - FastAPI → variable de entorno  NEXT_PUBLIC_API_URL=http://localhost:8000
 *
 *  🚩 TODO (Semana 10): cambia las rutas por las de tu backend real y adapta
 *  los campos a lo que devuelva. La estructura de estas funciones (try/catch,
 *  validación de status) es la MISMA que usarás en un proyecto de verdad.
 */

import type { Proyecto } from "@/data/proyectos";

const BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "";

/** Respuesta genérica de una API REST. */
export type RespuestaAPI<T> = {
  ok: boolean;
  datos?: T;
  error?: string;
};

export type NuevoProyecto = Omit<Proyecto, "id">;

/** GET: traer todos los proyectos. */
export async function getProyectos(): Promise<Proyecto[]> {
  const respuesta = await fetch(`${BASE_URL}/api/proyectos`, {
    // cache: "no-store" = no guardes en caché, quiero datos frescos.
    cache: "no-store",
  });

  if (!respuesta.ok) {
    throw new Error(`La API respondió con status ${respuesta.status}`);
  }

  const json = (await respuesta.json()) as { proyectos: Proyecto[] };
  return json.proyectos;
}

/** POST: crear un proyecto nuevo. */
export async function crearProyecto(datos: NuevoProyecto): Promise<Proyecto> {
  const respuesta = await fetch(`${BASE_URL}/api/proyectos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos),
  });

  if (!respuesta.ok) {
    throw new Error(`No se pudo crear el proyecto (status ${respuesta.status})`);
  }

  const json = (await respuesta.json()) as { proyecto: Proyecto };
  return json.proyecto;
}
