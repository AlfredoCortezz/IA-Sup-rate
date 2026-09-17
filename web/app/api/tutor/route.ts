/**
 * ============================================================
 *  ENDPOINT: /api/tutor — el "cerebro" del tutor de IA
 * ============================================================
 *  POST/JSON  { "mensaje": "¿por qué separar train y test?" }
 *  →          { ok: true, respuesta: "<pistas>" }
 *
 *  No llama a ninguna API externa: usa el corpus de `lib/tutor.ts`.
 *  Si algún día conectas un modelo real, sustituye buscarRespuesta()
 *  por la llamada a OpenAI/Groq pasándole el corpus como contexto.
 *
 *  🚩 TODO (Semana 10): puedes guardar el historial en memoria o en
 *  una base de datos y permitir "continuar la conversación".
 */

import { NextResponse } from "next/server";
import { buscarRespuesta } from "@/lib/tutor";

// No cachear: queremos respuesta siempre fresca.
export const dynamic = "force-dynamic";

export async function POST(request: Request) {
  const cuerpo = (await request.json()) as { mensaje?: string } | null;

  const mensaje = (cuerpo?.mensaje ?? "").trim();
  if (!mensaje) {
    return NextResponse.json(
      { ok: false, error: "Escribe una pregunta para poder ayudarte." },
      { status: 400 },
    );
  }

  const respuesta = buscarRespuesta(mensaje);
  return NextResponse.json({ ok: true, respuesta });
}