# -*- coding: utf-8 -*-
# ============================================================
#  AUTOCHEQUEO · Semana 8 — NLP (análisis de sentimiento)
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

titulo("AUTOCHEQUEO · Semana 8 — NLP (análisis de sentimiento)")

ruta, es_ipynb = encontrar_reto(CARPETA)
if ruta is None:
    error("No encontré reto_*.py ni reto_*.ipynb en la carpeta.")
    print("   Renombra tu archivo como reto_nlp.(py|ipynb) o re-clona la carpeta.")
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

# 2) Verificar la regla de oro (fit solo en train)
registrar("fit_transform(X_train" in contenido.replace(" ", ""),
          "El vectorizador aprende SOLO con el texto de entrenamiento (fit_transform en X_train).",
          sugerencia="La regla de oro: vectorizador.fit_transform(X_train) y luego solo .transform(X_test).")

# 3) ¿Corre sin errores?
print("\n🔎 Ejecutando tu reto...")
ok_run, salida, err = ejecutar_reto(ruta)
registrar(ok_run, "Tu script corre de principio a fin sin errores.",
          sugerencia=f"Al correr dio este mensaje:\n{err[-1200:]}")

if ok_run:
    baja = salida.lower()
    registrar(bool(re.search(r"[01]\.\d{2,}", salida)),
              "Se ve un número con decimales que podría ser tu accuracy.",
              sugerencia="Imprime el accuracy_score con una frase, p. ej.: print('Accuracy:', acc).")
    registrar("confusion" in baja or bool(re.search(r"\[\[", salida)),
              "Se ve la matriz de confusión (TP/TN/FP/FN).",
              sugerencia="Imprime confusion_matrix(y_test, y_pred).")
    registrar("positiva" in baja or "negativa" in baja,
              "Tu salida distingue reseñas POSITIVAS/NEGATIVAS.",
              sugerencia="En el paso de 'reseñas nuevas', muestra junto a cada frase la palabra POSITIVA o NEGATIVA.")

sys.exit(0 if resumen() else 1)