# 💼 Portafolio Next.js — Semanas 9 y 10

Proyecto **Next.js 15 + TypeScript**. Es tu portafolio personal y, al mismo
tiempo, un laboratorio para aprender cómo un frontend se conecta a una API.

---

## 🚀 Cómo arrancarlo

```bash
cd web
npm install      # solo la primera vez
npm run dev
```

Abre <http://localhost:3000>. (Detalle en `../tools/04-nextjs-y-vercel.md`.)

Otros comandos:

```bash
npm run build      # comprueba que todo esté bien (y lo prepara para producción)
npm run start      # corre la versión de producción
npm run typecheck  # revisa los tipos de TypeScript
```

## 🗂️ Estructura

```
web/
├── app/
│   ├── layout.tsx                 ← molde que envuelve todas las páginas
│   ├── globals.css                ← estilos globales (personalízalos)
│   ├── page.tsx                   ← TU portafolio (Semana 9)
│   └── api/proyectos/route.ts     ← API simulada GET/POST (Semana 10)
├── components/
│   ├── ProyectoCard.tsx           ← tarjeta de un proyecto
│   ├── ProyectoForm.tsx           ← formulario que hace POST
│   └── ProyectosSection.tsx       ← lista + formulario (estado y fetch)
├── data/proyectos.ts              ← ← ¡EMPIEZA AQUÍ! tus proyectos
└── lib/api.ts                     ← funciones getProyectos / crearProyecto
```

## 🧭 Ruta de trabajo

### Semana 9 — Construye tu portafolio
1. `data/proyectos.ts` → reemplaza los ejemplos por **tus** proyectos.
2. `app/page.tsx` → busca los `🚩 TODO` y pon tu nombre, frase y links.
3. `app/layout.tsx` → cambia el título de la pestaña.
4. `app/globals.css` → dale tu estilo (colores, fuentes).
5. Ejecuta `npm run build` y confirma que no hay errores.

### Semana 10 — Conecta la API y despliega
1. Lee `app/api/proyectos/route.ts`: ahí está el "backend" simulado.
2. Lee `lib/api.ts` y `components/ProyectosSection.tsx`: así se hace un `fetch`.
3. Agrega un proyecto desde el formulario y observa el `POST` (mira la pestaña
   **Network/Red** del navegador 🔍).
4. 🔥 Reto: implementa **DELETE** (`/api/proyectos/[id]`) o filtros por tecnología.
5. Despliega en **Vercel** (ver `../tools/04-nextjs-y-vercel.md`).

## 🔌 ¿Y un backend real (NestJS / FastAPI)?

Solo cambia la variable de entorno y la URL en `lib/api.ts`:

```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
```

El mismo endpoint se ve así en un backend de verdad:

- **NestJS**: un `@Controller("proyectos")` con `@Get()` y `@Post()`.
- **FastAPI**: un `@app.get("/api/proyectos")` y `@app.post("/api/proyectos")`.

La idea es idéntica a la del archivo `route.ts`: URL + método + JSON.

## ✅ Checklist de entrega

- [ ] `npm run build` pasa sin errores.
- [ ] Mi portafolio tiene mi nombre, mis proyectos y mi estilo.
- [ ] El formulario crea proyectos (POST) y la lista se recarga.
- [ ] Manejo el estado de **carga** y de **error**.
- [ ] Está desplegado en Vercel con link público.
