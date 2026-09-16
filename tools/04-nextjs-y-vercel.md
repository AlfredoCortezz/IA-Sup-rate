# 🚀 Next.js y Vercel — tu portafolio en internet (semanas 9–10)

El proyecto de las semanas 9 y 10 está en la carpeta **`web/`**. Es un proyecto
**Next.js** con **TypeScript**.

## De qué va (en 30 segundos)

| Tecnología | Para qué sirve |
|------------|----------------|
| **Next.js** | Un framework que convierte componentes (piezas de código) en páginas web reales |
| **TypeScript** | JavaScript "con tipos": te avisa de errores ANTES de ejecutar |
| **React** | La "magia" que repinta la pantalla cuando cambian los datos |
| **Vercel** | Servicio gratuito que sube tu proyecto a internet con un link público |

## Correr el proyecto en tu PC (primera vez)

```bash
# Navega a la carpeta web (desde la raíz del repo)
cd web

# Instala las dependencias (una sola vez; en herramientas del curso puede tardar)
npm install

# Enciende el servidor de desarrollo
npm run dev
```

Abre tu navegador en <http://localhost:3000> 🎉.

## Si algo no compila

```bash
npm run build          # verifica que todo esté correcto
npm run dev            # vuelve a arrancar el servidor
```

Si `build` da error, lee el error de **arriba hacia abajo**; casi siempre es un
tipo de TypeScript o un componente mal importado.

## Desplegar en Vercel (gratis, semanas 9–10)

1. Crea una cuenta en <https://vercel.com> (con GitHub es súper fácil).
2. Botón **Add New → Project**.
3. Importa tu repositorio de GitHub y selecciona la carpeta `web/` como
   **Root Directory**.
4. Deja todo por defecto y pulsa **Deploy**.
5. En menos de un minuto tendrás un link tipo `tu-proyecto.vercel.app` para
   presumirlo en el grupo 🥳.

> 💡 Cada vez que hagas `git push` a tu rama main, **Vercel vuelve a
> desplegar automáticamente**. Github + Vercel = tu código se publica solo.

## Estructura que verás en `web/`

```
web/
├── app/
│   ├── layout.tsx      ← el "esqueleto" que envuelve toda la página
│   ├── page.tsx        ← TU portafolio (Semana 9, cámbialo a tu estilo)
│   ├── globals.css     ← estilos globales
│   └── api/proyectos/route.ts  ← API de ejemplo (Semana 10: consúmela)
├── components/         ← piezas reutilizables (tarjeta, formulario…)
└── data/proyectos.ts   ← datos de ejemplo: reemplázalos por tus proyectos reales
```

> 🧪 **Reto relámpago:** corre `npm run dev` y cambia tu nombre en
> `app/page.tsx`. Si se ve en pantalla, ya hiciste tu primer cambio web.