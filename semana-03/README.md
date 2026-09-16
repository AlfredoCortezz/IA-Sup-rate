# 📈 Semana 3 — Regresión Lineal: adivina tu calificación

> **Misión:** enseñarle a una computadora a **predecir un número** (tu nota)
> a partir de tus horas de estudio. Tu primer modelo de Machine Learning real.

---

## 🎯 ¿Qué es la regresión lineal? (en 3 líneas)

Pones los datos en una gráfica y trazas la **recta que mejor pasa por en
medio**. Esa recta te deja predecir valores que nunca viste. La fórmula es:

$$calificación = 2.5 + 6.0 \times horas$$

Ese `6.0` (la **pendiente**) significa "cada hora extra sube 6 puntos". Ese es
todo el secreto. 🪄

## 🧰 Archivos de esta semana

| Archivo | Para qué |
|---------|----------|
| `reto_regresion_lineal.py` | El reto como script (córrelo con `python`) |
| `reto_regresion_lineal.ipynb` | El mismo reto en notebook (Google Colab / Jupyter) |

> ⚠️ Los dos tienen **el mismo contenido**. Elige el que prefieras
> (`tools/03-notebooks-y-scripts.md` te ayuda a decidir).

## 🚩 Cómo resolver el reto

Abre el archivo y busca las marcas `🚩 TODO`. Son **9 pasos**:

1. Importar las herramientas (ya está).
2. Crear el dataset (ya está).
3. Graficar y observar (ya está).
4. **Separar X e y** ← tú.
5. **train_test_split** ← tú.
6. **Crear y entrenar el modelo** ← tú.
7. **Predecir y medir MAE/R²** ← tú.
8. **Interpretar coeficiente e intercepto** ← tú.
9. **Dibujar la recta** ← tú.
10. 🔥 Reto extra: añadir `horas_sueno` como segunda característica.

> 💡 Cuando un `todo(...)` te detiene con `🚩 TODO pendiente`, NO es un error:
> es la señal de dónde debes escribir tu código.

## 📦 Entregables

1. `semana-03/ENTREGA.md` con:
   - Equipo e integrantes (con roles).
   - Tu **MAE** y tu **R²** finales.
   - Respuestas al **Autochequeo** (las 5 preguntas del final del código).
   - Una gráfica guardada (`figura_semana3.png`, con `plt.savefig`).
2. El archivo `.py` o `.ipynb` **completado y sin errores**.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 3 — Regresión Lineal · Equipo #N
| Integrante | Rol |
|------------|-----|
| ... | ... |

## Resultados
- MAE: __ puntos
- R²: __
- Pendiente: __ (significa: ...)
- Intercepto: __ (significa: ...)

## Autochequeo
1. El intercepto significa...
2. Separamos train/test porque...
3. Con test_size=0.9 pasaría... y con 0.05...
4. Nuestro MAE fue __ y R² __
5. ¿Serviría para casas? ...

## Reflexión del equipo (2 líneas)
...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| El código corre sin errores y completa los TODO | 8 |
| Mide y reporta MAE y R² correctamente | 5 |
| Interpreta pendiente/intercepto con sentido | 4 |
| Gráfica guardada + `ENTREGA.md` completo | 3 |

## ✅ Autochequeo rápido

- [ ] Entiendo qué es una feature (X) y una respuesta (y).
- [ ] Sé por qué separo datos de entrenamiento y de prueba.
- [ ] Puedo explicar qué significa mi pendiente.
- [ ] Tengo mi gráfica guardada como evidencia.
- [ ] `ENTREGA.md` subido en la rama `equipo-N-semana-03`.

> 🧪 **Reto relámpago:** antes de codificar, dibujen a mano una nube de puntos y
> una recta. Luego comparen con la que saca la máquina.