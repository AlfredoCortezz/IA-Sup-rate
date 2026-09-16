/**
 * ============================================================
 *  API SIMULADA — "backend" dentro del mismo proyecto Next.js
 * ============================================================
 *  Esto es un "Route Handler": una función que responde a una URL.
 *  Es exactamente igual a un endpoint de un backend real.
 *
 *  GET  /api/proyectos  → devuelve la lista de proyectos (JSON)
 *  POST /api/proyectos  → crea un proyecto
 *
 *  ⚠️ Los datos viven en memoria: si el servidor reinicia, se pierden.
 *  Para persistir de verdad necesitarías una base de datos (Postgres,
 *  MongoDB...). Aquí es solo para APRENDER cómo se conecta el frontend.
 *
 *  ------------------------------------------------------------
 *  ¿Y si tuvieras un backend de verdad? El mismo endpoint se vería así:
 *
 *  NestJS (TypeScript):
 *    @Controller("proyectos")
 *    export class ProyectosController {
 *      @Get()
 *      getAll() { return this.service.findAll(); }
 *
 *      @Post()
 *      create(@Body() dto: CrearProyectoDto) { return this.service.create(dto); }
 *    }
 *
 *  FastAPI (Python):
 *    @app.get("/api/proyectos")
 *    def listar(): return {"proyectos": proyectos}
 *
 *    @app.post("/api/proyectos")
 *    def crear(proyecto: ProyectoIn): ...
 *
 *  La idea es la MISMA: una URL + un método (GET/POST/DELETE) + JSON.
 *  ------------------------------------------------------------
 */

import { NextResponse } from "next/server";
import { proyectosIniciales, type Proyecto } from "@/data/proyectos";

// Estado en memoria (se reinicia con el servidor).
let proyectos: Proyecto[] = [...proyectosIniciales];
let siguienteId = proyectos.length + 1;

// Con esto evitamos que la respuesta se "congele" en caché.
export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json({ ok: true, proyectos });
}

export async function POST(request: Request) {
  // 🚩 TODO (Semana 10): valida el cuerpo (que el título no venga vacío,
  // que la descripción exista) y devuelve status 400 si está mal.
  const cuerpo = (await request.json()) as Partial<Proyecto>;

  if (!cuerpo.titulo || !cuerpo.descripcion) {
    return NextResponse.json(
      { ok: false, error: "El título y la descripción son obligatorios." },
      { status: 400 },
    );
  }

  const nuevo: Proyecto = {
    id: siguienteId++,
    titulo: cuerpo.titulo,
    descripcion: cuerpo.descripcion,
    tecnologias: cuerpo.tecnologias ?? [],
    emoji: cuerpo.emoji ?? "🚀",
    enlace: cuerpo.enlace,
    semana: cuerpo.semana ?? 10,
  };

  proyectos = [nuevo, ...proyectos];

  // 201 = "creado con éxito" (es el código correcto para un POST, no 200).
  return NextResponse.json({ ok: true, proyecto: nuevo }, { status: 201 });
}
