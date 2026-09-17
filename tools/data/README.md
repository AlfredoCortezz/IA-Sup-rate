# 📊 Banco de datasets (Semanas 3–8)

> Conjuntos **extra** con las MISMAS columnas que los retos, para repetir,
> ampliar o practicar. Los retos ya generan datos en su código; esta carpeta
> te da versiones más grandes para experimentar.

## Cómo re-generarlos (por si quieres otras semillas)

Desde la raíz del repo:

```bash
python tools/data/generar_datasets.py
```

Todos salen con `SEED = 42` → mismo resultado siempre.

## Los archivos

| Archivo | Semana | Filas | Columnas | ¿Para qué? |
|---------|--------|-------|----------|------------|
| `horas_sueno.csv` | 3 | 120 | `horas_estudio`, `horas_sueno`, `calificacion` | Reto extra de la regresión (2ª característica: horas de sueño) |
| `peliculas_ampliado.csv` | 5 | 120 | `titulo`, `year`, `accion`, `comedia`, `romance`, `duracion`, `rating` | KNN: predecir `rating` con más películas |
| `clientes_mall.csv` | 6 | 300 | `edad`, `gasto_mensual`, `visitas_por_mes` | K-Means: segmentar 300 clientes (en vez de 240) |
| `resenas_extra.csv` | 8 | 60 | `texto`, `sentimiento` (1=pos, 0=neg) | NLP: más reseñas para entrenar |
| `precios_casas.csv` | 5 (extra) | 150 | `m2`, `banos`, `antiguedad_anos`, `precio` | KNN de regresión sobre otro dominio |

## Cómo usarlo en un reto (un solo cambio)

**Semana 5** (`reto_knn.py`): sustituye el `catalogo` por

```python
catalogo = pd.read_csv("../../tools/data/peliculas_ampliado.csv")
```

**Semana 6** (`reto_kmeans.py`):

```python
df = pd.read_csv("../../tools/data/clientes_mall.csv")
```

**Semana 3** (reto extra de sueño):

```python
df = pd.read_csv("../../tools/data/horas_sueno.csv")
```

> 💡 Si trabajas en Google Colab o en una carpeta distinta, ajusta la ruta
> relativa para que apunte a `tools/data/` de tu copia del repo.

## Regla de oro al ampliar

- Semanas 5–6: **escala** con `StandardScaler` antes de distancia/clustering.
- Semana 3: controla que las columnas numéricas se llamen exactamente igual
  (`df.columns` te lo dice).
- Rellena los huecos si aparecen valores vacíos (`tools/06-errores-comunes.md` nº4).