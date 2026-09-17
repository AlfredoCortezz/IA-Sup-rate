# 💼 Semana 9 — Tu portafolio web con Next.js

> **Misión:** convertirte en desarrollador/a web frontend. Vas a construir tu
> **portafolio personal** con Next.js + TypeScript para mostrar todo lo que
> hiciste en el curso. Al final tendrá su propio link en internet.

---

## 🎯 ¿Qué es Next.js y por qué no HTML a secas?

En la Semana 1 usaste HTML directo: un archivo = una página. Está bien para
empezar, pero en proyectos grandes necesitas **componentes** (piezas
reutilizables) y TypeScript (que te avise de errores antes de ejecutar).

| Concepto | En cristiano |
|----------|--------------|
| **Componente** | Una función que devuelve HTML (una tarjeta, un botón, la página entera) |
| **Props** | Los datos que le pasas a un componente (`<ProyectoCard proyecto={p} />`) |
| **TypeScript** | JavaScript con tipos: si te equivocas, te lo dice el editor |
| **JSX/TSX** | Escribir HTML dentro de TypeScript |

## 🧰 Dónde está el proyecto

El proyecto vive en la carpeta **`web/`** (compartida con la Semana 10).

```bash
cd web
npm install     # solo la primera vez
npm run dev     # abre http://localhost:3000
```

> Si te atascas: `tools/04-nextjs-y-vercel.md`.

## 🚩 Los pasos de esta semana

Abre los archivos y busca los `🚩 TODO`:

1. **`data/proyectos.ts`** → cambia los 8 ejemplos por **tus proyectos reales**
   (los de las semanas 1–8). Ponles tu emoji, título y descripción.
2. **`app/page.tsx`** → pon tu **nombre**, tu **frase** y tus **links**.
3. **`app/layout.tsx`** → cambia el `title` (lo que sale en la pestaña).
4. **`app/globals.css`** → personaliza colores y fuentes. Hazlo TUYO.
5. **`components/ProyectoCard.tsx`** → mejora el diseño de las tarjetas.
6. Corre `npm run build` y comprueba que **no haya errores**.

## 📦 Entregables

1. Proyecto `web/` modificado con **tu** información (no la plantilla).
2. `semana-09/ENTREGA.md` con:
   - Equipo e integrantes.
   - Captura de tu portafolio con tus proyectos.
   - **Aportación personal** de cada integrante (qué cambió cada quien).
   - Respuestas al autochequeo.
3. `npm run build` sin errores (pega la salida final).

### Plantilla de `ENTREGA.md`

```markdown
# Semana 9 — Portafolio · Equipo #N
| Integrante | Qué cambió en el portafolio |
|------------|------------------------------|
| ... | colores + tarjetas |

## Captura
![portafolio](captura-portafolio.png)

## Build
```
 ✓ Compiled successfully
```

## Autochequeo
1. Un componente es... y sirve para...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| Portafolio personalizado (nombre, frase, links reales) | 6 |
| Proyectos propios cargados desde `data/proyectos.ts` | 5 |
| Edición de componentes y estilos | 5 |
| `npm run build` sin errores + `ENTREGA.md` | 4 |

## ✅ Autochequeo

- [ ] Puedo explicar qué es un componente y para qué sirven las props.
- [ ] Cambié el título en `layout.tsx` y se ve en la pestaña.
- [ ] Mi `data/proyectos.ts` tiene MIS proyectos, no los de ejemplo.
- [ ] `npm run build` termina sin errores.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-09`.

> 🧪 **Reto relámpago:** añade una sección nueva "🎮 Mis hobbies" usando un
> componente propio. ¿Te animas a que sea reutilizable con props?

---

## 🎬 Guías oficiales (mejor que cualquier video):

- [Next.js: Aprende](https://nextjs.org/learn) — el tutorial oficial (en español).
- [React: Escribe tus primeros componentes](https://es.react.dev/learn/your-first-component).

## 🤖 Pídele ayuda al tutor de IA

El tutor responde dudas de la parte web: *"¿qué es un componente?"*, *"¿para qué sirven las props?"*, etc.

## 📚 Apoyo si te atascas

- 📍 `tools/cheatsheets/03-nextjs.md` — componentes, "use client" y TypeScript en 1 página.
- 🚑 `tools/06-errores-comunes.md` — errores típicos de Next.js/npm (nº15–20).
- 🐍... bueno, esto ya no es Python: ¡bienvenidos al frontend!