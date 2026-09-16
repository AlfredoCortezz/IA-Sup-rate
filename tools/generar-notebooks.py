"""
Generador de notebooks (.ipynb) a partir de scripts .py en formato "percent".

USO (solo para el/la docente, no lo necesitan los estudiantes):

    python tools/generar-notebooks.py

Convierte cada `semana-XX/reto_*.py` en su `semana-XX/reto_*.ipynb`.

¿Por qué este formato? Porque los archivos `.py` ya usan las marcas
`# %%` que entiende VS Code (Python Interactive) y Jupyter, así que el mismo
archivo sirve para correr celda por celda sin duplicar el contenido a mano.
"""
import json
import pathlib
import sys


def py_a_notebook(texto: str) -> dict:
    """Convierte el texto de un .py en formato percent a un dict de notebook."""
    bloques = []          # lista de (tipo, [lineas])
    tipo_actual = "code"
    celda = []

    def cerrar():
        if celda:
            bloques.append((tipo_actual, list(celda)))
            celda.clear()

    for linea in texto.splitlines():
        if linea.startswith("# %%"):
            cerrar()
            tipo_actual = "markdown" if "markdown" in linea else "code"
        else:
            celda.append(linea)
    cerrar()

    celdas = []
    for tipo, lineas in bloques:
        while lineas and lineas[0].strip() == "":
            lineas.pop(0)
        while lineas and lineas[-1].strip() == "":
            lineas.pop()
        if not lineas:
            continue

        if tipo == "markdown":
            md = []
            for ln in lineas:
                if ln.startswith("# "):
                    md.append(ln[2:])
                elif ln.strip() == "#":
                    md.append("")
                else:
                    md.append(ln)
        else:
            md = lineas

        fuente = [ln + "\n" for ln in md]
        if tipo == "markdown":
            celdas.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": fuente,
            })
        else:
            celdas.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": fuente,
            })

    return {
        "cells": celdas,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.10"},
            "colab": {"provenance": []},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> int:
    raiz = pathlib.Path(__file__).resolve().parent.parent
    scripts = sorted(raiz.glob("semana-*/reto_*.py"))
    if not scripts:
        print("No encontré scripts semana-*/reto_*.py")
        return 1

    for script in scripts:
        nb = py_a_notebook(script.read_text(encoding="utf-8"))
        destino = script.with_suffix(".ipynb")
        destino.write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        print(f"OK  {script.relative_to(raiz)}  ->  {destino.name}  ({len(nb['cells'])} celdas)")
    return 0


if __name__ == "__main__":
    sys.exit(main())