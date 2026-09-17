# 🚑 tools/06 — Errores comunes (y cómo salir de ellos)

> **Antes de preguntarle al profe (o a cualquier IA), lee el error.**
> El 80 % de los errores de este curso caben en esta página. El truco no es
> aprenderlos de memoria: es aprender a **leer el mensaje** y buscar aquí
> palabras clave.

---

## 🐍 Errores de Python (lo que va a pasar en las Semanas 3–8)

### 1. `ValueError: Expected 2D array, got 1D array instead`
**Dónde:** Semana 3, al entrenar o predecir con `LinearRegression`.
**Por qué:** scikit-learn espera que `X` sea una **tabla 2D** (filas × columnas).
Si hiciste `X = df["horas_estudio"]` te dio una *serie* (1D).
**Arreglo:** doble corchete → `X = df[["horas_estudio"]]`.
📌 Memo: *serie* = 1D, *tabla* = 2D. El modelo quiere tabla.

### 2. `NameError: name 'pandas' is not defined`
**Por qué:** usaste `pandas.DataFrame(...)` pero importaste a medias.
**Arreglo:** `import pandas as pd`. Si importaste `pd` pero escribiste
`pandas...`, cambia por `pd...`. **El alias manda.**

### 3. `KeyError: 'calificacion'` (o cualquier columna)
**Por qué:** esa columna no existe en el DataFrame (¿entra mal? ¿mayúsculas?).
**Arreglo:** corre `print(df.columns)` y copia el nombre *exacto*.

### 4. `NaN` / `inf` y el modelo falla o da basura
**Dónde:** Semana 4 (Titanic) sobre todo.
**Arreglo:** usa `df.dropna(...)` o `df["age"].fillna(df["age"].median())`.
Verifica después: `df.isnull().sum()` debe dar `0`.

### 5. `AttributeError: 'DataFrame' object has no attribute 'map'`
**Arreglo:** `map` funciona sobre *series* (`df["sex"].map({...})`).
`DataFrame.map` no existe (en pandas nuevos es `DataFrame.applymap` o `df.replace`).

### 6. `ValueError: Input contains NaN, infinity or a value too large...`
Igual que el caso 4: hay huecos o valores infinitos. Limpia y vuelve a correr.

### 7. `EOFError` / `SyntaxError` raros en la consola
**Por qué:** casi siempre es un **paréntesis sin cerrar** o comillas mal abiertas
en una línea anterior.
**Arreglo:** cuenta los `(` y `)` de la línea, o borra la última línea y escrita
despacio.

### 8. La gráfica no sale / sale en blanco
**Por qué:** con `plt.savefig` primero y `plt.show` después. O la figura se
guardó antes de que existiera.
**Arreglo:**
```python
plt.savefig("mi_grafica.png", dpi=120)  # primero
plt.show()                               # después
```
Y usa nombres en inglés sin tildes ni espacios: `figura_semana3.png`, no
`figura semana 3!.png`.

### 9. `ModuleNotFoundError: No module named 'seaborn'` (o 'sklearn', 'pandas'…)
**Arreglo:**
```bash
pip install pandas numpy matplotlib scikit-learn seaborn
```
En Google Colab no hace falta: ya vienen instaladas.

### 10. "El código del .ipynb corre en Colab pero en mi PC no"
**No es magia:** Colab ya trae las librerías y Python 3.x. En tu PC asegúrate de
haber instalado las librerías (caso 9) y de ejecutar con el MISMO kernel de
Python 3 (no un Python viejo de Windows).

---

## 🌐 Errores de git (Semanas 1–10)

### 11. `fatal: not a git repository`
**Arreglo:** tienes que estar *dentro* de la carpeta clonada. `cd` hasta el
README.md (
`tools/01-git-y-github.md`).

### 12. `rejected - non-fast-forward` al hacer `git push`
**Por qué:** tu rama local y la remota se separaron.
**Arreglo (sin miedo):**
```bash
git pull --rebase origin <tu-rama>
git push origin <tu-rama>
```

### 13. `error: failed to push some refs to`
Común en rama que ya existe en GitHub. Mismo arreglo: `git pull --rebase` y
vuelve a `push`.

### 14. "Subí mil fotos/archivos sin querer"
```bash
git rm --cached <nombre-del-archivo>   # lo saca del control de versión
echo "<nombre>" >> .gitignore          # y nunca más se sube
```

---

## ⚛️ Errores de Next.js / npm (Semanas 9–10)

### 15. `'npm' is not recognized as an internal or external command`
**Arreglo:** instala Node.js desde <https://nodejs.org> (versión LTS) y **cierra
y abre la terminal**. `npm` viene junto con Node.

### 16. `npm ERR! code ENOENT` / `EMPATHY`
Te faltó `npm install` o estás en la carpeta equivocada. Verifica que
`package.json` exista (debe estar en `web/`):
```bash
cd web
npm install
npm run dev
```

### 17. `Module not found: Can't resolve '...'`
**Por qué:** importaste una ruta que no existe o te faltó un archivo.
**Arreglo:** revisa que la ruta coincida (mayúsculas importan) y que el archivo
esté creado. Si importas `@/components/X` asegúrate del archivo `X.tsx`.

### 18. `Type error` / `Type 'string | undefined' is not assignable to type 'string'`
Es TypeScript avisándote antes de tiempo (¡es TU amigo!).
**Arreglo:** el valor podría ser `undefined`; usa `?? "valor por defecto"` o
un `if`.

### 19. El `npm run build` falla pero el `npm run dev` funciona
Normal en Next.js: en build, TypeScript y el renderizado en servidor son más
estrictos. Busca el **primer** `Error` de la salida y corrígelo; normalmente es
un tipo o una API que falta.

### 20. `localhost:3000 no carga o dice "Cannot find module"`
Mata el proceso de `npm run dev` (`Ctrl+C`) y revisa en la termoinal que no
aparezca el error 16 o 17. Súele ser una instalación a medias: borra
`node_modules` y `package-lock.json` y repite `npm install`.

---

## 🧭 Cómo leer cualquier error (rutina de 3 pasos)

1. **LEE el mensaje completo** (no solo la última línea). Busca la palabra clave
   de la lista: `NameError`, `ValueError`, `KeyError`, `ModuleNotFoundError`,
   `TypeError`, `ENOENT`, `Type error`, `SyntaxError`.
2. **Busca esa palabra aquí arriba** y aplica el arreglo.
3. **Si sigue, ve al código:** el error casi siempre dice el archivo y la
   **línea** del problema (p. ej. `File "reto_regresion_lineal.py", line 126`).
   Revisa ESA línea y la anterior.

> 💡 **No borres el error.** Pégalo tal cual en tu pregunta al profe, tutor o
> IA. "Me sale un error en la línea 126" + el texto completo = respuesta en 1 minuto.

## 🧪 El mismo error en forma de reto

- [ ] Puedo explicar qué significa `ValueError` con mis palabras.
- [ ] Sé la diferencia entre *serie* (1D) y *tabla* (2D).
- [ ] Localizo el archivo y la **línea** de mi error sin que nadie me lo diga.
- [ ] He probado `pip install ...` antes de rendirme con un `ModuleNotFoundError`.
- [ ] Sé rescatar un `git push` rechazado con `pull --rebase`.