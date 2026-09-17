# -*- coding: utf-8 -*-
"""
tools/data/generar_datasets.py
==============================
Banco de datos EXTRA del curso (Semanas 3-8).

Los retos ya traen sus datos generados en el código. Aquí tienes conjuntos
MÁS GRANDES con las MISMAS columnas, para que puedas:

  - usar `pd.read_csv('../../tools/data/<archivo>.csv')` como alternativa,
  - repetir un reto con más datos,
  - practicar por tu cuenta.

Todos usan una semilla fija (SEED = 42) para que salgan SIEMPRE iguales.

Se ejecuta desde la raíz del repo:
    python tools/data/generar_datasets.py
"""

import numpy as np
import pandas as pd
import os

SEED = 42
rng = np.random.default_rng(SEED)
AQUI = os.path.dirname(os.path.abspath(__file__))

palabras_positivas = [
    "Me encantó, la historia es increíble y la actuación genial",
    "Una obra maestra, salí feliz y con ganas de repetir",
    "Excelente, cumplió todo lo que prometía, muy recomendado",
    "Increíble calidad, se nota el buen trabajo en cada detalle",
    "La mejor experiencia, superó todas mis expectativas",
    "Buenísimo, vale cada peso y lo recomiendo a todos",
    "Me dejó sin palabras, es de lo mejor que he visto",
    "Perfecto para un finde, me encantó de principio a fin",
    "Muy buena compra, funciona perfecto y llegó a tiempo",
    "Divertidísimo, el equipo me atendió con mucha amabilidad",
]

palabras_negativas = [
    "No me gustó nada, la historia es aburrida y los actores flojos",
    "Fue lo peor, perdí mi tiempo y mi dinero con esto",
    "Pésimo, nadie me atendió y llegó roto y tarde",
    "Malísimo, se rompió al segundo día, no lo compren",
    "Una decepción total, esperaba mucho más de lo que vi",
    "Terrible, todo salió mal y nadie se hizo responsable",
    "Mala calidad, muy caro para lo que ofrece",
    "No lo recomiendo para nada, fue un desastre completo",
    "Aburridísimo, casi me quedo dormido de lo malo que es",
    "Soplagaitas, no vale ni la mitad de lo que pagué",
]


def guardar(df, nombre):
    ruta = os.path.join(AQUI, nombre)
    df.to_csv(ruta, index=False)
    print(f"  generado {nombre}  ({len(df)} filas x {df.shape[1]} cols)")


# --------------------------------------------------------------------------
# 1) horas_sueno.csv  → Semana 3 (RE: reto extra con 2ª característica)
#    columnas: horas_estudio, horas_sueno, calificacion
# --------------------------------------------------------------------------
def generar_horas_sueno():
    n = 120
    horas_estudio = np.clip(rng.normal(4.7, 3.0, n), 0, 10).round(1)
    horas_sueno = np.clip(rng.normal(7.4, 1.5, n), 3, 12).round(1)
    base = 28.0 + 5.7 * horas_estudio + 1.3 * (horas_sueno - 7.4)
    calificacion = np.clip(base + rng.normal(0, 7, n), 0, 100).round(1)
    df = pd.DataFrame({
        "horas_estudio": horas_estudio,
        "horas_sueno": horas_sueno,
        "calificacion": calificacion,
    })
    return df.sort_values("horas_estudio").reset_index(drop=True)


# --------------------------------------------------------------------------
# 2) peliculas_ampliado.csv → Semana 5 (KNN sobre valoración)
#    columnas: titulo, year, accion, comedia, romance, duracion, rating
# --------------------------------------------------------------------------
def generar_peliculas():
    n = 120
    prefijos = ["La aventura de", "El misterio de", "Noche en", "Viaje a", "El regreso de"]
    sustantivos = ["Neptuno", "los Robots", "la Galaxia", "Casa Azul", "Terraza", "los Esquimales",
                   "Malibú", "Arcadia", "los Gemelos", "Polar", "la Isla", "Sofá"]
    noms = [f"{rng.choice(prefijos)} {rng.choice(sustantivos)}" for _ in range(n)]
    titulos = [f"Reto {i:03d}: {s}" for i, s in enumerate(noms)]
    year = rng.integers(1970, 2026, n)
    accion = np.clip(rng.integers(1, 11, n) + rng.normal(0, 1.2, n), 1, 10).round()
    comedia = np.clip(rng.integers(1, 11, n) + rng.normal(0, 1.2, n), 1, 10).round()
    romance = np.clip(rng.integers(1, 11, n) + rng.normal(0, 1.2, n), 1, 10).round()
    duracion = np.clip(rng.normal(105, 28, n), 70, 180).round().astype(int)
    rating = np.clip(
        6.2 + 0.28 * accion + 0.22 * comedia + 0.2 * romance + rng.normal(0, 0.9, n),
        3.5, 9.9,
    ).round(1)
    df = pd.DataFrame({
        "titulo": titulos,
        "year": year,
        "accion": accion.astype(int),
        "comedia": comedia.astype(int),
        "romance": romance.astype(int),
        "duracion": duracion,
        "rating": rating,
    })
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)


# --------------------------------------------------------------------------
# 3) clientes_mall.csv → Semana 6 (K-Means, más grande)
#    columnas: edad, gasto_mensual, visitas_por_mes
# --------------------------------------------------------------------------
def generar_clientes():
    n = 300
    centros = [
        (22, 420, 6),   # estudiantes
        (28, 950, 11),  # compradores frecuentes
        (42, 750, 8),   # ejecutivos/seguidores moderados
        (62, 220, 3),   # jubilados tranquilos
    ]
    Xs, Ys, Vs = [], [], []
    for _ in range(n):
        cent = centros[rng.integers(0, len(centros))]
        Xs.append(np.clip(rng.normal(cent[0], 3.5), 16, 90))
        Ys.append(np.clip(rng.normal(cent[1], 85), 80, 1400))
        Vs.append(np.clip(rng.normal(cent[2], 1.6), 1, 18))
    df = pd.DataFrame({
        "edad": np.round(Xs, 0).astype(int),
        "gasto_mensual": np.round(Ys, 0).astype(int),
        "visitas_por_mes": np.round(Vs, 0).astype(int),
    })
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)


# --------------------------------------------------------------------------
# 4) resenas_extra.csv → Semana 8 (análisis de sentimiento)
#    columnas: texto, sentimiento  (1 = positiva, 0 = negativa)
# --------------------------------------------------------------------------
def generar_resenas():
    n = 60
    textos, sentis = [], []
    for i in range(n):
        if rng.random() < 0.5:
            textos.append(f"{rng.choice(palabras_positivas)} #{i}.")
            sentis.append(1)
        else:
            textos.append(f"{rng.choice(palabras_negativas)} #{i}.")
            sentis.append(0)
    df = pd.DataFrame({"texto": textos, "sentimiento": sentis})
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)


# --------------------------------------------------------------------------
# 5) precios_casas.csv → extra (KNN de regresión alternativo)
#    columnas: m2, banos, antiguedad_anos, precio
# --------------------------------------------------------------------------
def generar_casas():
    n = 150
    m2 = np.clip(rng.normal(110, 45, n).round(), 35, 320).astype(int)
    banos = np.clip(rng.normal(2.0, 0.8, n).round(), 1, 5).astype(int)
    antiguedad = np.clip(rng.normal(18, 14, n).round(), 0, 60).astype(int)
    precio = np.clip(
        38_000 + 1_850 * m2 + 25_000 * banos - 350 * antiguedad + rng.normal(0, 28_000, n),
        60_000, 950_000,
    ).round(-3)
    df = pd.DataFrame({
        "m2": m2,
        "banos": banos,
        "antiguedad_anos": antiguedad,
        "precio": precio.astype(int),
    })
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)


if __name__ == "__main__":
    print("Generando datasets con SEED =", SEED)
    guardar(generar_horas_sueno(), "horas_sueno.csv")
    guardar(generar_peliculas(), "peliculas_ampliado.csv")
    guardar(generar_clientes(), "clientes_mall.csv")
    guardar(generar_resenas(), "resenas_extra.csv")
    guardar(generar_casas(), "precios_casas.csv")
    print("¡Listo! Revisa la descripción de cada uno en tools/data/README.md")