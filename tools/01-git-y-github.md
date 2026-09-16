# 🐙 Git y GitHub — La máquina del tiempo de tu código

**Git** guarda "fotos" (commits) de tu proyecto. **GitHub** es una nube donde
guardas esas fotos para que tu equipo vea el mismo proyecto.

## Vocabulario mínimo (60 segundos)

| Término | Qué es, en cristiano |
|---------|----------------------|
| `repo` | El proyecto completo (esta carpeta) |
| `commit` | Una foto guardada de tu trabajo |
| `push` | Subir tus fotos a GitHub |
| `pull` | Bajar las fotos que otros subieron |
| `branch` (rama) | Una versión paralela del proyecto (copias de seguridad) |
| `clone` | Copiar un repo de GitHub a tu PC |

## Los 6 comandos que usarás el 95% del tiempo

```bash
# 1) ¿Qué archivos cambié?
git status

# 2) ¿Qué cambio dentro de un archivo?
git diff

# 3) Preparar los archivos que quiero guardar
git add .

# 4) Guardar la foto con un mensaje bonito
git commit -m "Semana 4: resuelvo TODO del Titanic"

# 5) Subir a GitHub (en tu rama de equipo)
git push origin main

# 6) Traer lo que hizo tu compañero
git pull origin main
```

## Flujo de trabajo recomendado para cada reto

1. **Clonar** una sola vez el repo del profe:
   ```bash
   git clone <url-del-repo>
   ```
2. **Crea tu rama de equipo** (uno por equipo):
   ```bash
   git checkout -b equipo-1-semana-04
   ```
3. Trabaja, y al terminar:
   ```bash
   git add .
   git commit -m "Semana 4 resuelta por el equipo 1"
   git push -u origin equipo-1-semana-04
   ```
4. Crea un **Pull Request** en GitHub para que el profe revise (botón verde "Compare & pull request").

## ⚠️ Errores típicos (y cómo no llorar)

- **"Olvidé qué archivos cambié"** → `git status` en la terminal.
- **"Borré algo sin querer"** → si ya lo habías hecho commit, `git restore <archivo>`.
- **"Quiero deshacer el último commit"** → `git reset --soft HEAD~1` (no pierde tu trabajo).
- **"Dos compañeros editaron el mismo archivo"** → HABLEN ANTES entre el equipo; los conflictos se arreglan conversando, no con magia.

> 🧪 **Reto relámpago:** crea un archivo `team.txt`, haz un commit y súbelo. `tools/01` está resuelto cuando tus compañeros también ven tu archivo.