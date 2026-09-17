# -*- coding: utf-8 -*-
# ============================================================
#  AUTOCHEQUEO · Semana 3 — Regresión Lineal
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

titulo("AUTOCHEQUEO · Semana 3 — Regresión Lineal")

ruta, es_ipynb = encontrar_reto(CARPETA)
if ruta is None:
    error("No encontré reto_*.py ni reto_*.ipynb en la carpeta.")
    print("   Renombra tu archivo como reto_regresion_lineal.(py|ipynb) o re-clona la carpeta.")
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
print("\n🔎 Ejecutando tu reto (las gráficas se dibujan sin abrir ventanas)...")
ok_run, salida, err = ejecutar_reto(ruta)
registrar(ok_run, "Tu script corre de principio a fin sin errores.",
          sugerencia=f"Al correr dio este mensaje:\n{err[-1200:]}")

if ok_run:
    baja = salida.lower()
    registrar("mae" in baja,
              "Aparece el MAE en la salida (búscalo en un print).",
              sugerencia="Imprímelo con una frase, p. ej.: print('MAE:', mae)")
    registrar(bool(re.search(r"r\s*\^?\s*2|r\u00b2", salida, re.I)),
              "Aparece el R² en la salida.",
              sugerencia="Imprímelo con una frase, p. ej.: print('R2:', r2)")
    registrar("coef" in baja or "pendiente" in baja,
              "Se imprimen el coeficiente / pendiente.",
              sugerencia="Usa modelo.coef_ dentro de un print.")
    registrar("intercept" in baja or "ordenada" in baja,
              "Se imprimen el intercepto / ordenada.",
              sugerencia="Usa modelo.intercept_ dentro de un print.")
    registrar(os.path.exists(os.path.join(CARPETA, "figura_semana3.png")),
              "La gráfica de la recta está guardada como figura_semana3.png.",
              sugerencia="En el paso 9 añade plt.savefig('figura_semana3.png') antes de plt.show().")
    registrar("horas_sueno" in baja,
              "Intentaste el 🔥 reto extra (horas de sueño como 2ª característica).",
              sugerencia="El extra es opcional, pero sube nota. ¡Aunque sea una línea, anótalo!")

sys.exit(0 if resumen() else 1)