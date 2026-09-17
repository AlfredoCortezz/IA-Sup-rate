# 🖨️ Git — Cheatsheet de bolsillo (Semanas 1–10)

> Imprimible: una página para tener al lado mientras trabajas.

## Los 4 mandamientos del workflow

| Comando | Qué hace | Cuándo |
|---------|----------|--------|
| `git clone <url>` | Copia el repo a tu PC | Una sola vez al inicio |
| `git status` | Muestra qué cambió | **Siempre antes de commitear** |
| `git add <archivo>` | Prepara un archivo para guardar | Antes de `commit` |
| `git commit -m "mensaje"` | Guarda una "foto" con mensaje | Cada vez que algo funcione |
| `git push origin <rama>` | Sube tu foto a GitHub | Al terminar el reto |

## El ritual completo (para cada reto)

```bash
git status                                     # 1) ¿qué tengo?
git add semana-03/ENTREGA.md semana-03/reto*.py   # 2) prepara lo que importa
git commit -m "Semana 3: reto de regresión completado"
git push origin equipo-3-semana-03             # 3) súbelo a tu rama
```

> ⚠️ `git add .` sube TODO. Si no quieres subir algo, no uses `.`
> (o ponlo en `.gitignore`).

## Ramas (tu espacio personal)

```bash
git branch                       # ¿en qué rama estoy?
git checkout -b equipo-3-semana-03   # crear y moverte a una rama nueva
git checkout equipo-3-semana-03      # volver a una rama
```

## Rescates (cuando algo se rompe)

| Situación | Comando |
|-----------|---------|
| Manda error el `push` porque se separaron las ramas | `git pull --rebase origin <rama>` y luego `git push` |
| Commit equivoqué el mensaje (¡todavía no lo subí!) | `git commit --amend -m "mensaje nuevo"` |
| Borré un archivo sin querer | `git checkout -- <archivo>` |
| Quiero ver el historial | `git log --oneline` |
| Se me olvidó un archivo en el último commit | `git add <archivo> && git commit --amend --no-edit` |

## Trampa común de novatos

- `git commit` sin `git add` → no guarda nada (el "espacio de preparación" existe).
- `git push` sin `commit` → no sube nada.
- Escribir el mensaje SIN `-m` → te abre un editor raro. Para salir de vim:
  escribe `:q` y Enter (o usa siempre `-m "..."`).

## Glosario exprés

- **repo / repositorio** → tu carpeta versionada.
- **commit** → una "foto guardada" del estado de tus archivos.
- **rama / branch** → una línea de trabajo separada.
- **push** → subir a GitHub.
- **pull** → traer cambios de GitHub a tu PC.
- **merge** → mezclar una rama con otra.
- **staging (add)** → el "antesala" del commit.

> 🧪 Practica en <https://learngitbranching.js.org/es> (gratis, en español).