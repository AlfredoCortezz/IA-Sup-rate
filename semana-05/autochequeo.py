# -*- coding: utf-8 -*-
# ============================================================
#  AUTOCHEQUEO · Semana 5 — KNN (recomendador de películas)
#  Feedback inmediato para tu equipo. NO da la solución.
#  Uso:  python autochequeo.py
# ============================================================
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))

from autochequeo_lib import (  # noqa: E402
    encontrar_reto,
    convertir_ipynb,
    ejecutar_reto,
    todos_pendientes,
    titulo,
    registrar,
    resumen,
    error,
    ok,
)

CARPETA = os.path.dirname(os.path.abspath(__file__))

titulo("AUTOCHEQUEO · Semana 5 — KNN (recomendador de películas)")

ruta, es_ipynb = encontrar_reto(CARPETA)
if ruta is None:
    error("No encontré reto_*.py ni reto_*.ipynb en la carpeta.")
    print("   Renombra tu archivo como reto_knn.(py|ipynb) o re-clona la carpeta.")
    sys.exit(1)
if es_ipynb:
    print("Encontré el .ipynb. Intento convertirlo a .py para analizarlo...")
    nueva = convertir_ipynb(CARPETA, ruta)
    if nueva:
        ruta = nueva
    else:
        print("Solo hay .ipynb y no tengo jupyter instalado. Corre:  pip install jupyter")
        sys.exit(1)

with open(ruta, encoding="utf-8", errors="replace") as f:
    contenido = f.read()

# 1) ¿Quedan TODO sin resolver?
pendientes = todos_pendientes(contenido)
if pendientes:
    error(f"Todavía hay {len(pendientes)} TODO sin resolver. Aquí están los que faltan:")
    for num, desc in pendientes[:8]:
        print(f"   Línea {num:>4}: {desc}")
    resumen()
    sys.exit(1)
ok("No quedan TODO pendientes en el código.")

# 2) ¿La función recomendar está definida?
registrar("def recomendar" in contenido,
          "La función recomendar(titulo, k) está definida.",
          sugerencia="Sin ella el reto no está completo: define def recomendar(titulo, k=3):")

# 3) ¿Corre sin errores?
print("\n🔎 Ejecutando tu reto...")
ok_run, salida, err = ejecutar_reto(ruta)
registrar(ok_run, "Tu script corre de principio a fin sin errores.",
          sugerencia=f"Al correr dio este mensaje:\n{err[-1200:]}")

if ok_run:
    baja = salida.lower()
    registrar("mae" in baja,
              "Aparece el MAE del regresor KNN en la salida.",
              sugerencia="Imprímelo con una frase, p. ej.: print('MAE:', mae)")
    registrar("matrix" in baja,
              "Mencionas a 'Matrix' (las recomendaciones del ejemplo).",
              sugerencia="En el reto se recomiendan películas parecidas a Matrix. Añádelo para comparar.")
    registrar("k=1" in baja or "k=3" in baja or "k=7" in baja.replace(" ", "") or "n_neighbors=" in baja.replace(" ", ""),
              "Experimentaste con el valor de k.",
              sugerencia="El reto extra pide probar k=1, k=3 y k=7 y ARGUMENTAR cuál funciona mejor.")

sys.exit(0 if resumen() else 1)