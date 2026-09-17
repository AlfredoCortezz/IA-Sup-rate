# 🤖 IA Sup-rate — Curso de IA y Desarrollo Web (10 semanas)

Plantilla de retos semanales para **bachillerato (16–18 años)**. Cada semana
tiene una misión práctica, un esqueleto de código con comentarios didácticos y
marcas `TODO` donde tú, junto con tu equipo, debes resolver la tarea.

> 🎯 **Regla de oro:** el repositorio nunca te da la respuesta final. Te da la
> **estructura, las pistas y el camino**. La magia la haces tú (y tus 3
> compañeros de equipo).

---

## 🗺️ Cómo está organizado el repositorio

```
IA-Sup-rate/
├── README.md              ← estás aquí (índice maestro)
├── tools/                 ← guías de apoyo si te atascas + pistas + cheatsheets + datasets
├── semana-01/             ← Qué es la IA de verdad (rompe el mito)
├── semana-02/             ← IA Generativa: Prompt Battle
├── semana-03/             ← Regresión Lineal (predicción de calificaciones)
├── semana-04/             ← Árbol de Decisión (Titanic 🚢)
├── semana-05/             ← KNN (recomendador de películas 🎬)
├── semana-06/             ← K-Means (segmentación de clientes 🛒)
├── semana-07/             ← Redes Neuronales (dígitos MNIST 🔢)
├── semana-08/             ← NLP (sentimiento de reseñas 💬)
├── semana-09/             ← Next.js: tu primer portafolio 💼 (está en web/)
├── semana-10/             ← Conecta una API y despliega en Vercel 🚀 (en web/)
└── web/                   ← proyecto Next.js + TypeScript de las semanas 9–10
```

## 📅 Ruta de aprendizaje (las 3 fases)

| Fase | Semanas | Qué aprendes | Herramientas |
|------|---------|--------------|--------------|
| 🧠 Desmitificación | 1 – 2 | Qué es (y qué no es) la IA, mitos, IA generativa e ingeniería de prompts | HTML/JS, Teachable Machine |
| 📈 Machine Learning | 3 – 8 | Modelos clásicos de ML desde cero | Python, scikit-learn, pandas, matplotlib |
| 🌐 Desarrollo Web | 9 – 10 | Tu portafolio web y el consumo de APIs | Next.js, TypeScript, Vercel |

## 👥 Trabajo en equipos de 4

Cada equipo debe decidir **quién hace qué** en cada reto. Rótalo cada semana:

| Rol | Responsabilidad |
|-----|-----------------|
| 🧑‍💻 **Capitán / Integrador** | Organiza, junta las piezas del equipo y sube el reto a GitHub |
| 🔬 **Investigador(a)** | Busca teoría, documenta y cita fuentes |
| 🛠️ **Código / Datos** | Se encarga del código, la limpieza de datos y las pruebas |
| 📢 **Presentador(a)** | Prepara la explicación final y defiende el reto ante el grupo |

> Cada semana debes rotar de rol mínimo 1 vez en las 10 semanas.

## 🤖 Tú tutor de IA

El proyecto `web/` trae un **chat de IA** (botón 🤖 abajo a la derecha) que
responde con pistas sobre teoría, errores y pistas de los retos. Corre con:

```bash
cd web
npm install     # solo la primera vez
npm run dev     # abre http://localhost:3000
```

También hay un **📊 panel de progreso** (`web/app/progreso`) y un
**autochequeo automático** en cada `semana-03` a `semana-08`.

## ✅ Cómo entregar un reto (checklist general)

1. Clona el repositorio (`tools/01-git-y-github.md` te explica cómo).
2. Lee el `README.md` de tu `semana-XX/`.
3. Completa las marcas `TODO` del código en equipo.
4. Corre tu código y comprueba que el **autochequeo** (si lo tiene) pasa.
5. Escribe en `ENTREGA.md` quiénes participaron y qué hizo cada quién.
6. Haz `commit` y `push` a una rama propia: `equipo-<número>-semana-XX`.
7. Presenta el reto en 3 minutos al grupo.

## 🆘 ¿Perdido? Mira las guías

- `tools/01-git-y-github.md` → clonar, commit, push (nunca más miedo a git)
- `tools/02-python-y-colab.md` → correr Python en tu PC o en Google Colab
- `tools/03-notebooks-y-scripts.md` → qué es un `.ipynb` y cómo usarlo
- `tools/04-nextjs-y-vercel.md` → correr `web/` y desplegarlo gratis
- `tools/05-vocabulario-ia.md` → glosario de la IA en cristiano
- `tools/06-errores-comunes.md` → errores típicos y cómo salir de ellos
- `tools/pistas/` → pistas escalonadas de los retos 3–8
- `tools/cheatsheets/` → hojas de referencia de git, Python y Next.js
- `tools/data/` → datasets extra para practicar
- Los **videos recomendados** están al final del `README.md` de cada semana 🎬

## 📜 Licencia

Uso educativo. Puedes copiar, adaptar y compartir citando el origen.