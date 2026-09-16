# 🧠 Semana 7 — Redes Neuronales: leer dígitos (MNIST)

> **Misión:** construir y entrenar tu primera **red neuronal**, y ponerla a leer
> números escritos a mano. El clásico "hola mundo" de la IA. 🔢

---

## 🎯 ¿Qué es una red neuronal (versión simple)?

Un equipo de **neuronas diminutas** organizadas en capas. Cada pixel entra,
cada neurona multiplica por **pesos** y vota, y la última capa elige el dígito
más probable. Entrenar = ajustar esos pesos para acertar.

```
pixeles → [capa oculta de neuronas] → "es un 7" (81 %)
```

> ℹ️ Usamos `MLPClassifier` de scikit-learn **para entender el concepto** sin
> pelearse con frameworks pesados. En producción se usa TensorFlow/PyTorch, pero
> la idea (capas + pesos + votos) es la misma.

## 🧰 Archivos

| Archivo | Para qué |
|---------|----------|
| `reto_mnist.py` | El reto como script |
| `reto_mnist.ipynb` | El mismo reto como notebook (recomendado: Colab) |

> ⚠️ `fetch_openml("mnist_784")` **descarga internet** la primera vez (queda en
> caché). Si falla, el código tiene **plan B**: usa `load_digits` (8×8), que ya
> viene instalado. Ideal para Google Colab.

## 🚩 Los pasos

1. Cargar MNIST con plan B (ya está).
2. Ver los dígitos como imágenes (ya está).
3. **Normalizar** los pixeles a 0–1 ← tú.
4. **Separa train/test con `stratify`** ← tú.
5. **Definir la red** (`MLPClassifier`, capas ocultas) ← tú.
6. **Entrenar** ← tú.
7. **Evaluar**: accuracy + matriz de confusión ← tú.
8. 🔥 Reto: probar arquitecturas `(32,)`, `(64,)`, `(128, 64)`, `(256,128,64)`.

## 📦 Entregables

1. `semana-07/ENTREGA.md`:
   - Equipo e integrantes.
   - **Accuracy** final de tu mejor red y qué configuración usaron.
   - La **matriz de confusión** (imagen o tabla) y los dígitos más confundidos.
   - Tabla del reto de arquitecturas con precisiones y tiempos.
   - Respuestas al autochequeo.
2. Al menos **2 imágenes**: una de los dígitos de ejemplo y una de los errores.
3. El `.py` o `.ipynb` completado.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 7 — MNIST · Equipo #N
| Integrante | Rol |
|------------|-----|

## Resultados
- Mejor arquitectura: (128, 64) con max_iter=30
- Accuracy: __ %
- Dígitos que más confundimos: __ con __

## Experimentos
| Arquitectura | max_iter | Accuracy | Tiempo aprox. |
|--------------|----------|----------|---------------|
| (32,) | 20 | | |
| (64,) | 20 | | |
| (128, 64) | 30 | | |

## Autochequeo
1. Cada imagen tiene __ entradas porque...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| Normalización y split con `stratify` correctos | 4 |
| Red definida y entrenada sin errores | 6 |
| Evaluación con accuracy + matriz de confusión | 5 |
| Experimentación de arquitecturas con conclusión | 5 |

## ✅ Autochequeo

- [ ] Sé cuántos valores de entrada tiene cada imagen y por qué.
- [ ] Puedo explicar qué hace una neurona (peso × entrada + voto).
- [ ] Entiendo para qué normalizamos.
- [ ] Comparé al menos 3 arquitecturas y saqué conclusiones.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-07`.

> 🧪 **Reto relámpago:** ¿qué dígitos se confunden más entre sí (4/9, 3/8, 1/7)?
> Dibújalos lado a lado y verás que ¡a ti también te cuestan!