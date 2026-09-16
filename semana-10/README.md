# 🚀 Semana 10 — Conecta una API y publica tu portafolio en Vercel

> **Misión final:** que tu portafolio **pida y envíe datos a una API** (como lo
> hacen las apps de verdad) y luego **publicarlo en internet** con un link
> público para compartirlo con el mundo. 🌍

---

## 🎯 ¿Qué vas a aprender?

Cómo dos programas conversan por internet con **REST**:

```
  NAVEGADOR (tu portafolio)                 SERVIDOR (la API)
        │                                        │
        │  GET /api/proyectos ──────────────────►│  devuelve JSON con la lista
        │  ◄──────────────────────────  {proyectos: [...]}
        │                                        │
        │  POST /api/proyectos (con datos) ─────►│  crea uno nuevo (status 201)
        │  ◄──────────────────────────  {proyecto: {...}}
```

| Método | Para qué |
|--------|----------|
| `GET` | Leer/traer datos |
| `POST` | Crear algo nuevo |
| `DELETE` | Borrar |
| `PUT` / `PATCH` | Actualizar |

## 🧰 Qué mirar (ya está todo montado)

| Archivo | Qué enseña |
|---------|------------|
| `web/app/api/proyectos/route.ts` | El "backend" simulado (GET y POST) |
| `web/lib/api.ts` | Las funciones que llaman a la API (`fetch`) |
| `web/components/ProyectosSection.tsx` | Estados de carga, error y recarga |
| `web/components/ProyectoForm.tsx` | El formulario que hace `POST` |

> 🔍 **Truco de detective:** abre la pestaña **Network** (o Red) del navegador,
> agrega un proyecto desde el formulario y **mira la petición POST**. Verás el
> JSON viajando. ¡Eso es una API en vivo!

## 🚩 Los pasos

1. `npm run dev` y agrega un proyecto con el **formulario** (mira la petición en Network).
2. Lee `app/api/proyectos/route.ts` y contesta: ¿qué pasa si falta el título?
3. 🔥 **Reto de código:** implementa el método **DELETE** creando
   `app/api/proyectos/[id]/route.ts` y un botón "🗑️" en la tarjeta.
4. 🔥 **Reto extra:** un filtro por tecnología o un buscador.
5. **Despliega en Vercel** (`tools/04-nextjs-y-vercel.md`) y comparte el link.

## 📦 Entregables

1. `semana-10/ENTREGA.md` con:
   - Equipo e integrantes.
   - El **link público de Vercel** (¡lo más importante!).
   - Captura de la pestaña **Network** mostrando el `GET` y el `POST`.
   - Qué reto extra hicieron (DELETE / filtro / buscador).
   - Respuestas al autochequeo.
2. Proyecto `web/` subido a GitHub con el despliegue funcionando.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 10 — API + Vercel · Equipo #N
| Integrante | Rol |
|------------|-----|

## 🌐 Link de producción
https://tu-portafolio.vercel.app

## Evidencia
- GET a /api/proyectos: (captura)
- POST desde el formulario: (captura)

## Reto extra
Implementamos DELETE porque...

## Autochequeo
1. La diferencia entre GET y POST es...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| El portafolio **carga proyectos** desde la API (GET) | 5 |
| El formulario **crea** proyectos (POST) y muestra estados | 5 |
| **Desplegado en Vercel** y link público funcionando | 6 |
| Reto extra (DELETE/filtro) + `ENTREGA.md` completo | 4 |

## ✅ Autochequeo

- [ ] Entiendo la diferencia entre `GET` y `POST`.
- [ ] Sé qué es un status `200`, `201` y `400`.
- [ ] Mi app muestra "Cargando..." y maneja el error si la API falla.
- [ ] Mi portafolio está **público en Vercel**.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-10`.

> 🎓 **Cierre del curso:** comparte tu link con la clase y explica en 3 minutos
> cuál fue **tu** aportación a cada fase (desmitificación, ML, web). ¡Lo lograste!
