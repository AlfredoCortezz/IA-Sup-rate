# IA Sup-rate · Curso de IA y Desarrollo Web (10 semanas)

Plantilla de retos semanales para estudiantes de bachillerato (16 a 18 años).
Cada semana tiene una misión práctica, un esqueleto de código con marcas `TODO`
y la parte correspondiente de la guía oficial de ejercicios
(`guia-semana-XX.pdf`), dividida por semana.

Regla general: el repositorio nunca entrega la respuesta final. Proporciona la
estructura, las pistas y el camino; el trabajo lo realiza cada equipo.

## Organización del repositorio

```
IA-Sup-rate/
├── README.md                ← índice maestro del curso
├── tools/                   ← guías de apoyo, pistas, cheatsheets y datasets
├── web/                     ← proyecto Next.js + TypeScript (semanas 9–10)
├── semana-01/               ← Qué es la IA de verdad (examen en línea)
├── semana-02/               ← IA generativa: Prompt Battle
├── semana-03/               ← Regresión lineal (predicción de calificaciones)
├── semana-04/               ← Árbol de decisión (Titanic)
├── semana-05/               ← KNN (recomendador de películas)
├── semana-06/               ← K-Means (segmentación de clientes)
├── semana-07/               ← Redes neuronales (dígitos MNIST)
├── semana-08/               ← NLP (sentimiento de reseñas)
├── semana-09/               ← Portafolio con Next.js (en web/)
└── semana-10/               ← API y despliegue en Vercel (en web/)
```

Cada carpeta `semana-XX/` contiene:

- `README.md` — instrucciones de la semana y forma de entrega.
- `guia-semana-XX.pdf` — teoría, ejercicios, rúbrica y autochequeo (parte de la
  guía oficial de ejercicios).
- Los archivos del reto (código, dashboard o notebook).

## Ruta de aprendizaje

| Fase | Semanas | Contenido | Herramientas |
|------|---------|-----------|--------------|
| Desmitificación | 1–2 | Qué es la IA, mitos, IA generativa e ingeniería de prompts | HTML/JS, Teachable Machine |
| Machine Learning | 3–8 | Modelos clásicos de ML desde cero | Python, scikit-learn, pandas, matplotlib |
| Desarrollo Web | 9–10 | Portafolio web y consumo de APIs | Next.js, TypeScript, Vercel |

## Trabajo en equipos de 4

Cada equipo decide quién hace qué en cada reto y rota los roles cada semana.

| Rol | Responsabilidad |
|-----|-----------------|
| Capitán / Integrador | Organiza, junta las piezas del equipo y sube el reto a GitHub |
| Investigador(a) | Busca teoría, documenta y cita fuentes |
| Código / Datos | Se encarga del código, la limpieza de datos y las pruebas |
| Presentador(a) | Prepara la explicación final y defiende el reto ante el grupo |

## Entrega semanal (cada estudiante crea su propia rama)

Para la evaluación, cada estudiante trabaja y entrega en su **propia rama**; no
se hace `push` a `main`.

```bash
git clone https://github.com/AlfredoCortezz/IA-Sup-rate.git
cd IA-Sup-rate
git checkout -b tu-nombre-semana-XX     # crea TU rama
```

Se completan las marcas `TODO` del reto, se agrega el `ENTREGA.md` (y la
evidencia, como el PDF del reporte de las semanas 1–2) y se realiza:

```bash
git add .
git commit -m "Entrega semana XX - <tu nombre>"
git push origin tu-nombre-semana-XX
```

Después se avisa al docente (pull request o enlace de la rama). Cada semana se
debe rotar de rol mínimo una vez.

### Semana 1: examen en línea

La entrega de la primera semana es el **examen en línea** de `semana-01`. Se
abre `semana-01/index.html` en el navegador desde la laptop, se responde el
cuestionario (un solo intento) y se descarga el reporte en PDF como evidencia.
Los pasos completos están en `semana-01/README.md`.

## Pasos generales de un reto

1. Clona el repositorio (`tools/01-git-y-github.md` explica cómo).
2. Lee el `README.md` de tu `semana-XX/`.
3. Estudia la teoría de `guia-semana-XX.pdf`.
4. Completa las marcas `TODO` del código en equipo.
5. Corre tu código y comprueba que el autochequeo (si lo tiene) pasa.
6. Escribe el `ENTREGA.md` con quienes participaron y qué hizo cada quien.
7. Haz `commit` y `push` a tu rama propia.
8. Presenta el reto en 3 minutos al grupo.

## Guías de apoyo

- `tools/01-git-y-github.md` — clonar, commit y push.
- `tools/02-python-y-colab.md` — correr Python en tu PC o en Google Colab.
- `tools/03-notebooks-y-scripts.md` — qué es un `.ipynb` y cómo usarlo.
- `tools/04-nextjs-y-vercel.md` — correr `web/` y desplegarlo gratis.
- `tools/05-vocabulario-ia.md` — glosario de la IA.
- `tools/06-errores-comunes.md` — errores típicos y cómo salir de ellos.
- `tools/pistas/` — pistas escalonadas de los retos 3–8.
- `tools/cheatsheets/` — hojas de referencia de git, Python y Next.js.
- `tools/data/` — datasets extra para practicar.

## Licencia

Uso educativo. Se puede copiar, adaptar y compartir citando el origen.