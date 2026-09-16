# 💬 Semana 8 — NLP: análisis de sentimiento

> **Misión:** enseñarle a una computadora a distinguir una reseña **positiva**
> de una **negativa**. La base de los filtros de spam y de los moderadores de
> comentarios. 🗣️

---

## 🎯 ¿Qué es NLP?

**Natural Language Processing** = hacer que la máquina trabaje con texto humano.
El problema central: las computadoras entienden **números**, no letras. Así que
convertimos texto → números (**vectorizar**) y clasificamos.

| Vectorizador | Qué hace |
|--------------|----------|
| `CountVectorizer` | Cuenta cuántas veces aparece cada palabra |
| `TfidfVectorizer` | Cuenta, pero resta peso a palabras comunes ("de", "la") |

> ⚠️ **Regla de oro (¡sale en la rúbrica!):** `fit` del vectorizador se hace SOLO
> con el texto de entrenamiento. Si no, sería "hacer trampa".

## 🧰 Archivos

| Archivo | Para qué |
|---------|----------|
| `reto_nlp.py` | El reto como script |
| `reto_nlp.ipynb` | El mismo reto como notebook |

## 🚩 Los pasos

1. Dataset de reseñas (ya está).
2. **Separar train/test** ← tú.
3. **Vectorizar** (`TfidfVectorizer`) ← tú.
4. **Entrenar** `MultinomialNB` ← tú.
5. **Evaluar** (accuracy + matriz de confusión) ← tú.
6. Probar reseñas **nuevas** escritas por el equipo ← tú.
7. 🔥 Reto: palabras más positivas y más negativas.

## 📦 Entregables

1. `semana-08/ENTREGA.md`:
   - Equipo e integrantes.
   - **Accuracy** del modelo.
   - Las 3 reseñas nuevas del equipo y su predicción.
   - Las **5 palabras** más asociadas a cada sentimiento.
   - Respuestas al autochequeo.
2. El `.py` o `.ipynb` completado.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 8 — NLP · Equipo #N
| Integrante | Rol |
|------------|-----|

## Resultados
- Accuracy: __ %
- Palabras positivas: ...
- Palabras negativas: ...

## Nuestras reseñas nuevas
| Reseña | Predicción | ¿Estuvimos de acuerdo? |
|--------|------------|------------------------|
| ... | POSITIVA | Sí |

## Autochequeo
1. Convertimos texto a números porque...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| `fit`/`transform` correctamente usados (sin trampa) | 6 |
| Modelo entrenado y evaluado | 5 |
| Predicción de reseñas nuevas funcionando | 5 |
| Aportación individual (2 reseñas por integrante) + reflexión | 4 |

## ✅ Autochequeo

- [ ] Puedo explicar por qué el texto se convierte en números.
- [ ] Sé la diferencia entre `fit_transform` y `transform`.
- [ ] Añadí 2 reseñas propias al dataset.
- [ ] Encontré las palabras "delatoras" de cada sentimiento.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-08`.

> 🧪 **Reto relámpago:** escriban una reseña con **sarcasmo** ("qué maravilla,
> se rompió a la primera"). ¿El modelo acierta? ¿Por qué el sarcasmo es
> dificilísimo para la IA? Guárdenlo para la discusión de la Semana 9.