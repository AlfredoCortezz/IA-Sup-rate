# -*- coding: utf-8 -*-
"""
Biblioteca compartida por los autochequeos de las semanas 3 a 8.

Un autochequeo es un script SIN nota: su trabajo es dar FEEDBACK INMEDIATO
al estudiante. Comprueba que el reto corre sin errores, que no quedan TODO
pendientes y que aparecen en pantalla las partes importantes (MAE, accuracy,
gráficas guardadas, etc.). NUNCA revela el código de la solución.

Los scripts `semana-XX/autochequeo.py` de cada semana importan las funciones
de aquí y definen qué verificar en SU reto.

Uso local (dentro de una carpeta semana-XX):
    python autochequeo.py
"""
import os
import re
import subprocess
import sys

# La consola de Windows usa cp1252 y se atraganta con emojis/acentos.
# Fuerza UTF-8 con reemplazo para que TODO se imprima sin romperse.
for _flujo in ("stdout", "stderr"):
    try:
        getattr(sys, _flujo).reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Colores (desactivados en Windows por compatibilidad de consola)
VERDE = "\033[92m" if os.name != "nt" else ""
AMARILLO = "\033[93m" if os.name != "nt" else ""
ROJO = "\033[91m" if os.name != "nt" else ""
RESET = "\033[0m" if os.name != "nt" else ""


def ok(mensaje):
    print(f"{VERDE}✅ {mensaje}{RESET}")


def aviso(mensaje):
    print(f"{AMARILLO}⚠️  {mensaje}{RESET}")


def error(mensaje):
    print(f"{ROJO}❌ {mensaje}{RESET}")


def titulo(nombre):
    ancho = 58
    print("=" * ancho)
    print(nombre.center(ancho))
    print("=" * ancho)


def encontrar_reto(carpeta):
    """Busca el archivo del reto dentro de la carpeta.

    Devuelve (ruta_al_script, es_ipynb). Prefiere el `.py`; si solo existe el
    `.ipynb`, devuelve ese (luego se intenta convertir). Si no hay nada sale
    con (None, None).
    """
    try:
        nombres = sorted(os.listdir(carpeta))
    except FileNotFoundError:
        return None, None

    py = [n for n in nombres if re.fullmatch(r"reto_[A-Za-z0-9_]+\.py", n)]
    if py:
        return os.path.join(carpeta, py[0]), False

    ipynb = [n for n in nombres if re.fullmatch(r"reto_[A-Za-z0-9_]+\.ipynb", n)]
    if ipynb:
        return os.path.join(carpeta, ipynb[0]), True

    return None, None


def convertir_ipynb(carpeta, ruta_ipynb):
    """Intenta convertir el .ipynb a .py con jupyter (si está instalado)."""
    try:
        import importlib.util  # noqa: F401  (solo para verificar numpy arriba)

        subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "script",
                ruta_ipynb,
            ],
            capture_output=True,
            text=True,
            cwd=carpeta,
            timeout=300,
        )
    except Exception:
        return None

    base = os.path.splitext(os.path.basename(ruta_ipynb))[0] + ".py"
    salida = os.path.join(carpeta, base)
    return salida if os.path.exists(salida) else None


def ejecutar_reto(ruta_py, timeout=900):
    """Corre el reto como subproceso y devuelve (ok, salida, error_salida).

    Usa el backend de matplotlib 'Agg' para que las gráficas NO abran ventanas
    y la ejecución no se quede esperando a que alguien las cierre.
    """
    env = dict(os.environ)
    env["MPLBACKEND"] = "Agg"
    try:
        p = subprocess.run(
            [sys.executable, ruta_py],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            cwd=os.path.dirname(ruta_py) or ".",
            env=env,
        )
        return p.returncode == 0, p.stdout or "", p.stderr or ""
    except subprocess.TimeoutExpired:
        return False, "", "⏱️  El script tardó demasiado. ¿Hay un bucle infinito o una descarga muy lenta?"


def todos_pendientes(contenido):
    """Lista de (número_de_línea, descripción) de los TODO que siguen sin resolver."""
    pendientes = []
    for num, linea in enumerate(contenido.splitlines(), 1):
        if re.search(r"\btodo\s*\(", linea) and not re.match(r"\s*def\s+todo\s*\(", linea):
            m = re.search(r'todo\("([^"]+)"\)', linea)
            desc = m.group(1) if m else linea.strip()
            pendientes.append((num, desc))
    return pendientes


# ----------------------------------------------------------------------------
# Registro de resultados para el resumen final
# ----------------------------------------------------------------------------
_RESULTADOS = []


def registrar(condicion, mensaje, sugerencia=None):
    if condicion:
        ok(mensaje)
        _RESULTADOS.append(True)
    else:
        error(mensaje)
        if sugerencia:
            aviso(sugerencia)
        _RESULTADOS.append(False)


def resumen():
    """Imprime el resumen y devuelve True si TODO pasó (para el exit code)."""
    print("\n" + "-" * 58)
    if not _RESULTADOS:
        error("No hubo comprobaciones que hacer.")
        return False
    aprobados = sum(_RESULTADOS)
    if aprobados == len(_RESULTADOS):
        ok(f"🎉 Autochequeo superado ({aprobados}/{len(_RESULTADOS)})."
           " Listo para preparar tu ENTREGA.md y tu presentación.")
        return True
    error(f"Autochequeo NO superado ({aprobados}/{len(_RESULTADOS)})")
    aviso("Revisa los ❌ de arriba y vuelve a intentarlo.")
    aviso("¿Atascado? → tools/pistas/semana-XX.md tiene pistas escalonadas.")
    aviso("¿Error raro? → tools/06-errores-comunes.md explica los fallos típicos.")
    return False