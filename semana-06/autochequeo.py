# -*- coding: utf-8 -*-
# ============================================================
#  AUTOCHEQUEO · Semana 6 — K-Means (segmentación de clientes)
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

titulo("AUTOCHEQUEO · Semana 6 — K-Means (segmentación de clientes)")

ruta, es_ipynb = encontrar_reto(CARPETA)
if ruta is None:
    error("No encontré reto_*.py ni reto_*.ipynb en la carpeta.")
    print("   Renombra tu archivo como reto_kmeans.(py|ipynb) o re-clona la carpeta.")
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

# 2) ¿Corre sin errores?
print("\n🔎 Ejecutando tu reto...")
ok_run, salida, err = ejecutar_reto(ruta)
registrar(ok_run, "Tu script corre de principio a fin sin errores.",
          sugerencia=f"Al correr dio este mensaje:\n{err[-1200:]}")

if ok_run:
    baja = salida.lower()
    registrar("inertia" in baja or "codo" in baja,
              "Aparece la inercia o el codo (método del codo) por pantalla.",
              sugerencia="Guarda la inercia de cada k y dibújala. La 'esquina' te dice el k óptimo.")
    registrar("cluster" in baja,
              "Mencionas 'cluster' en la salida.",
              sugerencia="Asigna df['cluster'] = modelo.labels_ y llévalo contigo a la gráfica y al groupby.")
    registrar(bool(re.search(r"ejecutiv|estudiante|jóven|joven|jubil|oferta", baja, re.I)),
              "Pusiste nombres humanos a los clusters (¡la parte de negocio!).",
              sugerencia="El reto pide BAUTIZAR cada grupo según sus promedios (edad, gasto, visitas).")
    registrar("labels_" in contenido or '"cluster"' in contenido or "'cluster'" in contenido,
              "El código asigna etiquetas de cluster al DataFrame.",
              sugerencia="Revisa que guardes df[\"cluster\"] = modelo.labels_ para poder graficar cada grupo de un color.")

sys.exit(0 if resumen() else 1)