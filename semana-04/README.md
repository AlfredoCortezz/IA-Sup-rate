# 🌳 Semana 4 — Árbol de Decisión: el Titanic 🚢

> **Misión:** entrenar un modelo que decida **¿sobreviviría esta persona?**
> usando un árbol de decisiones, e **interpretar** cómo razona.

---

## 🎯 ¿Qué es un árbol de decisión?

Es el juego de las **20 preguntas** convertido en IA. El modelo aprende cuál
pregunta separa mejor a los sobrevivientes de los que no:

```
¿Eres mujer?  ──Sí──►  ¿3ª clase?  ──No──►  SOBREVIVIÓ
     │                     └──Sí──►  MURIÓ
     └──No──►  ¿Eres niño?  ──Sí──►  SOBREVIVIÓ
                    └──No──►  MURIÓ
```

Ventaja enorme: puedes **ver** y **explicar** por qué decidió lo que decidió.

## 🧰 Archivos

| Archivo | Para qué |
|---------|----------|
| `reto_titanic.py` | El reto como script |
| `reto_titanic.ipynb` | El mismo reto como notebook (Colab/Jupyter) |

> El dataset viene incluido en `seaborn` (`sns.load_dataset("titanic")`), no
> necesitas descargar nada a mano.

## 🚩 Los pasos (busca los `TODO` en el código)

1. Cargar el dataset (ya está).
2. Explorar supervivencia por sexo y clase (ya está).
3. **Preparar los datos**: elegir features, convertir `sex` a números, manejar los `age` nulos.
4. **Separar X / y** y `train_test_split`.
5. **Crear el árbol** con `max_depth=3` y entrenarlo.
6. **Evaluar**: `accuracy_score`, `confusion_matrix`, `classification_report`.
7. **Dibujar el árbol** con `plot_tree` y guardarlo (`arbol_titanic.png`).
8. 🔥 Reto: comparar `max_depth` de 1 a 10 y **ver el sobreajuste**.

## 📦 Entregables

1. `semana-04/ENTREGA.md` con equipo, integrantes y roles, más:
   - `accuracy` final y su comparación con el "baseline" (decir siempre "no").
   - La **primera pregunta (raíz)** de tu árbol y una explicación.
   - Tabla del reto de `max_depth`: profundidad → accuracy train/test.
   - Respuestas al autochequeo.
2. La imagen `arbol_titanic.png`.
3. El `.py` o `.ipynb` completado.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 4 — Titanic · Equipo #N
| Integrante | Rol |
|------------|-----|
| ... | ... |

## Resultados
- Accuracy del árbol: __ %
- Baseline ("todos mueren"): ~62 %
- Primera pregunta del árbol: ¿...?
- ¿Por qué la eligió? ...

## Sobreajuste (max_depth)
| Profundidad | Accuracy train | Accuracy test |
|-------------|----------------|---------------|
| 1 | | |
| 3 | | |
| 10 | | |
| sin límite | | |

## Autochequeo
1. ...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| Preprocesamiento correcto (nulos y texto→número) | 5 |
| El modelo entrena y se evalúa bien | 6 |
| Árbol dibujado e interpretado | 6 |
| `ENTREGA.md` + reflexión individual | 3 |

## ✅ Autochequeo

- [ ] Sé qué es una "hoja" y la "raíz" del árbol.
- [ ] Puedo explicar por qué convertimos `sex` a 0/1.
- [ ] Entiendo el sobreajuste y lo vi en la tabla.
- [ ] Mi árbol está guardado como imagen.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-04`.

> 🧪 **Reto relámpago:** antes de correr el código, apuesten: ¿qué 3 columnas
> creen que predecirán mejor la supervivencia? Comparen con lo que eligió el árbol.