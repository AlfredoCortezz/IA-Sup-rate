# -*- coding: utf-8 -*-
# ============================================================
#  AUTOCHEQUEO · Semana 7 — Red Neuronal (MNIST)
#  Feedback inmediato para tu equipo. NO da la solución.
#  Uso:  python autochequeo.py
#  ⏱️  Este reto tarda: entrena una red neuronal de verdad.
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

titulo("AUTOCHEQUEO · Semana 7 — Red Neuronal (MNIST)")

ruta, es_ipynb = encontrar_reto(CARPETA)
if ruta is None:
    error("No encontré reto_*.py ni reto_*.ipynb en la carpeta.")
    print("   Renombra tu archivo como reto_mnist.(py|ipynb) o re-clona la carpeta.")
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

# 2) ¿Se normaliza y se usa stratify? (se deduce del código)
registrar("255" in contenido or "max()" in contenido or "/ 255" in contenido,
          "El código normaliza los pixeles (división para dejarlos entre 0 y 1).",
          sugerencia="La normalización suele verse como X_norm = X_todo / X_todo.max() o / 255.")
registrar("stratify" in contenido,
          "Se usa stratify en el train_test_split.",
          sugerencia="stratify=y_todo mantiene la misma proporción de dígitos en train y test.")

# 3) ¿Corre sin errores? (¡puede tardar 1-3 minutos!)
print("\n🔎 Ejecutando tu reto. Si descarga MNIST, espera un poco...")
ok_run, salida, err = ejecutar_reto(ruta, timeout=1200)
registrar(ok_run, "Tu red neuronal entrena y corre sin errores.",
          sugerencia=f"Al correr dio este mensaje:\n{err[-1200:]}")

if ok_run:
    baja = salida.lower()
    registrar(bool(re.search(r"[01]\.\d{2,}", salida)),
              "Se ve un número con decimales que podría ser tu accuracy.",
              sugerencia="Imprime el accuracy_score con una frase, p. ej.: print('Accuracy:', acc).")
    registrar("confusion" in baja or bool(re.search(r"\[\[", salida)),
              "Se ve la matriz de confusión.",
              sugerencia="Imprime confusion_matrix(y_test, y_pred) para ver qué dígitos se confunden.")
    registrar("architectur" in baja or "hidden_layer" in contenido or "(128" in contenido,
              "Experimentaste con la arquitectura de la red.",
              sugerencia="El reto pide probar (32,), (64,), (128, 64)... y comparar accuracy y tiempo.")

sys.exit(0 if resumen() else 1)