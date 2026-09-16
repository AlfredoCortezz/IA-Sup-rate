# 🎬 Semana 5 — KNN: recomendador de películas

> **Misión:** construir un sistema que, dada una película que te gusta, te
> recomiende otras parecidas. Tu primer "Netflix casero" 🍿.

---

## 🎯 La idea

**KNN = K-Nearest Neighbors ("los K vecinos más cercanos")**. Para decidir algo
sobre una película, miramos las **K más parecidas** y nos fijamos en ellas.

- Para **recomendar** → devolvemos las vecinas.
- Para **predecir el rating** → promediamos el rating de las vecinas.

## ⚠️ Concepto clave: escalar los datos

Si `year` va de 1990 a 2020 y `accion` de 0 a 10, ¡el año domina la distancia! El
modelo ignoraría los géneros. Con `StandardScaler` ponemos todo en la misma
escala. **Este es el aprendizaje más importante de la semana.**

## 🧰 Archivos

| Archivo | Para qué |
|---------|----------|
| `reto_knn.py` | El reto como script |
| `reto_knn.ipynb` | El mismo reto como notebook |

> El catálogo está **dentro del código** (16 películas). Añade tus favoritas.

## 🚩 Los pasos

1. Catálogo de películas (ya está).
2. **Elegir las características** (`year`, `accion`, `comedia`, `romance`) ← tú.
3. **Escalar** con `StandardScaler` ← tú.
4. **Encontrar vecinas** con `NearestNeighbors` ← tú.
5. **Predecir rating** con `KNeighborsRegressor` ← tú.
6. **Programar la función `recomendar(titulo, k)`** ← tú.
7. 🔥 Reto: comparar `k=1`, `k=3`, `k=7`.

## 📦 Entregables

1. `semana-05/ENTREGA.md`:
   - Equipo e integrantes (con roles).
   - Las **3 recomendaciones** de "Matrix" y de una película que elijan.
   - El **MAE** del regresor KNN.
   - Respuestas al autochequeo.
2. El `.py` o `.ipynb` completado y funcionando.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 5 — KNN · Equipo #N
| Integrante | Rol |
|------------|-----|

## Recomendaciones
- Si te gustó **Matrix**, mira: ... porque ...
- Nuestra película favorita: ... → recomendadas: ...

## Resultados
- MAE del modelo: __
- ¿Cambia con k=7? ...

## Autochequeo
1. KNN necesita escalar porque...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| Escala correctamente (fit/transform bien usados) | 5 |
| Encuentra vecinos y recomienda con la misma escala | 6 |
| Entrena y evalúa el regresor KNN | 5 |
| `ENTREGA.md` con reflexión individual | 4 |

## ✅ Autochequeo

- [ ] Explico por qué el escalado es obligatorio en KNN.
- [ ] Entiendo la diferencia entre `fit_transform` y `transform`.
- [ ] Mi función `recomendar()` no se recomienda a sí misma.
- [ ] Probé varios valores de `k`.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-05`.

> 🧪 **Reto relámpago:** ¿qué características añadirías al catálogo para mejorar
> las recomendaciones (actor favorito, saga, duración)? Anótenlas para la clase.