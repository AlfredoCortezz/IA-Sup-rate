# ⚛️ Next.js + TypeScript — Cheatsheet (Semanas 9–10)

> Imprimible: todo lo que repites en el portafolio y su API.

## 1. Comandos del día a día

```bash
npm install          # instala dependencias (solo la 1ª vez)
npm run dev          # servidor local → http://localhost:3000
npm run build        # compila "para producción" (comprueba errores)
npm run typecheck    # revisa los tipos TypeScript
```

> Si `npm` no existe → instala Node.js LTS y **reabre la terminal**.

## 2. Anatomía de una página (App Router)

| Archivo | Qué es |
|---------|--------|
| `app/page.tsx` | La página principal (`/`) |
| `app/layout.tsx` | El "molde" que envuelve todo (html, body, metadatos) |
| `app/progreso/page.tsx` | Otra página en `/progreso` |
| `app/api/.../route.ts` | Un endpoint de API (GET/POST/...) |
| `components/**` | Piezas reutilizables |

## 3. Componente (función que devuelve HTML)

```tsx
// components/Tarjeta.tsx
type Props = { titulo: string; enlace?: string };

export function Tarjeta({ titulo, enlace }: Props) {
  return (
    <article>
      <h3>{titulo}</h3>
      {enlace && <a href={enlace}>Ver →</a>}
    </article>
  );
}
```

Se usa así: `<Tarjeta titulo="Mi proyecto" enlace="https://..." />`

> `Props` = los datos que entran al componente. Si no llegan, se ven vacíos.

## 4. Componentes "use client" vs servidor

```tsx
"use client";   // ← primera línea: usa useState, onClick... (corre en el navegador)

import { useState } from "react";
const [contador, setContador] = useState(0);
```

- **Sin** `"use client"` → componente de servidor (más rápido, no hay estado).
- **Con** `"use client"` → puede interactuar (formularios, clicks, chats).

## 5. Consumir una API (fetch)

```ts
const resp = await fetch(`${BASE_URL}/api/proyectos`, { cache: "no-store" });
if (!resp.ok) throw new Error(`Status ${resp.status}`);
const json = await resp.json();
return json.proyectos;
```

> `cache: "no-store"` = datos frescos cada vez (importante tras un POST).

## 6. Crear un endpoint de API (route.ts)

```ts
import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({ ok: true, proyectos });
}

export async function POST(request: Request) {
  const cuerpo = await request.json();
  if (!cuerpo.titulo) {
    return NextResponse.json({ error: "Falta el título" }, { status: 400 });
  }
  return NextResponse.json({ ok: true }, { status: 201 });
}
```

### Códigos de estado que debes conocer

| Código | Significado |
|--------|-------------|
| `200` | Todo bien (GET) |
| `201` | Creado (POST) |
| `400` | Petición mala (faltan datos) |
| `404` | No encontrado |
| `500` | Error del servidor |

## 7. TypeScript en 60 segundos

```ts
let nombre: string = "Ana";          // tipos explícitos
let notas: number[] = [8, 9, 7];
let proyecto: { titulo: string; semana: number } = { titulo: "X", semana: 3 };
let link: string | undefined;        // unión: puede no estar
link ?? "default";                   // ?? = valor por defecto si es null/undefined
```

> `string | undefined` + usar el valor sin `??` → error de TypeScript. **Ese
> error es el editor cuidándote.** Arreglo: `valor ?? "fallback"`.

## 8. TypeScript en el JSON (objeto tipado)

```ts
export type Proyecto = {
  id: number;
  titulo: string;
  tecnologias: string[];
  emoji?: string;   // opcional
};
```

## 9. Desplegar en Vercel (el final del curso)

1. Sube tu repo a GitHub (`git push` de tu rama).
2. Entra a <https://vercel.com> → **Add New** → **Project**.
3. Importa tu repo, elige el framework **Next.js** y pulsa **Deploy**.
4. ¡Link público gratis! Cada `push` a la rama principal lo actualiza solo.

> Guía completa: `tools/04-nextjs-y-vercel.md`.

## 10. Checklist para tus 3 minutos de presentación

- [ ] `npm run build` sin errores.
- [ ] Mi nombre y mi link reales en `app/page.tsx`.
- [ ] Mis proyectos reales en `data/proyectos.ts`.
- [ ] El formulario crea proyectos y veo el POST en la pestaña Network.
- [ ] Está desplegado en Vercel y abro el link público.