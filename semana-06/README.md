# 🛒 Semana 6 — K-Means: segmentación de clientes

> **Misión:** agrupar 240 clientes en "tipos de persona" **sin que nadie te diga
> cuáles son los grupos**. Descubre los patrones por tu cuenta. 🔍

---

## 🎯 ¿Qué es K-Means y qué lo hace distinto?

K-Means agrupa puntos parecidos alrededor de **centroides** (los promedios del
grupo). A diferencia de las semanas 3–5, aquí **no hay respuestas correctas**:
es **aprendizaje no supervisado**.

| Supervisado (S3–S5) | No supervisado (S6) |
|---------------------|---------------------|
| Con etiquetas | Sin etiquetas |
| Predice | Descubre grupos |

## 🧰 Archivos

| Archivo | Para qué |
|---------|----------|
| `reto_kmeans.py` | El reto como script |
| `reto_kmeans.ipynb` | El mismo reto como notebook |

> Los clientes son **ficticios** y se generan con `make_blobs`. No hay descargas.

## 🚩 Los pasos

1. Generar clientes (ya está).
2. Graficar (ya está).
3. **Escalar** ← tú.
4. **Método del codo** para elegir k ← tú.
5. **Entrenar K-Means** y pintar los grupos ← tú.
6. **Interpretar y nombrar** cada segmento ← tú.
7. 🔥 Reto: `silhouette_score` y comparar con los grupos "secretos".

## 📦 Entregables

1. `semana-06/ENTREGA.md`:
   - Equipo e integrantes.
   - La gráfica del **codo** (`codo_kmeans.png`) y qué k eligieron.
   - La gráfica de **clusters coloreados** (`clusters_clientes.png`).
   - La tabla `groupby(...).mean()` y los **nombres** de cada segmento.
   - Respuestas al autochequeo.
2. El `.py` o `.ipynb` completado.

### Plantilla de `ENTREGA.md`

```markdown
# Semana 6 — K-Means · Equipo #N
| Integrante | Rol |
|------------|-----|

## Elección de k
El codo se ve en k=__. Elegimos k=__ porque...

## Nuestros segmentos
| Cluster | Edad prom. | Gasto prom. | Visitas | Nombre que le pusimos |
|---------|------------|-------------|---------|------------------------|
| 0 | | | | |

## Autochequeo
1. Supervisado = ... No supervisado = ...
```

## 📊 Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| Escalado correcto | 4 |
| Codo bien interpretado | 5 |
| Clusters graficados y coherentes | 5 |
| Nombres de segmentos justificados con los promedios | 6 |

## ✅ Autochequeo

- [ ] Sé qué es un centroide.
- [ ] Puedo explicar por qué necesitamos escalar (otra vez).
- [ ] Mi codo tiene una explicación, no solo "porque sí".
- [ ] Los nombres de mis clusters se basan en los promedios reales.
- [ ] `ENTREGA.md` subido en `equipo-N-semana-06`.

> 🧪 **Reto relámpago:** ¿para qué crees que una tienda usa esto? Escribe un
> ejemplo de campaña distinta para cada uno de tus segmentos.