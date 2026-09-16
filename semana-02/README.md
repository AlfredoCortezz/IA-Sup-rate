# 🤖 Semana 2 — IA Generativa: tu copiloto (Prompt Battle)

> **Misión del reto:** entender cómo "piensa" una IA generativa (tokens,
> embeddings, atención) y demostrar que dominas el arte del **prompt**.
> Todo se juega y se califica en un solo archivo: `dashboard-semana2.html`.

---

## 1. Teoría que debes dominar (¡sale en el quiz!)

| Concepto | En cristiano |
|----------|--------------|
| **Token** | La unidad mínima de texto. "casa" ≈ 1 token; "increíblemente" puede ser 3. Los modelos cuentan y predicen por tokens, no por palabras. |
| **Embedding** | Convertir palabras en listas de números para que la máquina capte relaciones: `rey − hombre + mujer ≈ reina`. |
| **Atención** | El mecanismo que decide **qué palabras importan más** para predecir la siguiente. |
| **Ingeniería de prompts** | Escribir con **rol + contexto + restricciones + formato**. Un prompt vago = respuesta vaga. |
| **Alucinación** | La IA inventa datos con seguridad total. No miente: completa texto "probable". ¡Verifica siempre! |
| **Sesgo** | El modelo hereda prejuicios de datos mal balanceados. |
| **Ética** | Si el prompt es discriminatorio, el resultado también. Somos responsables del uso. |

> Lee `tools/05-vocabulario-ia.md` (filas de la Semana 2) y esta tabla. El quiz
> del dashboard sale **exactamente** de aquí.

## 2. Cómo funciona el dashboard 🎮

Abre **`dashboard-semana2.html`** (doble clic o arrástralo al navegador).
Tiene 3 fases y las tres cuentan para tu nota:

### 🟦 Fase A — Evaluación Teórica (bloquea el resto)
- 3 preguntas de opción múltiple (Tokens, Alucinaciones, Sesgos).
- El dashboard **califica solo**. Necesitas **≥ 2 aciertos** para desbloquear
  la Fase B.
- Son 3 puntos → valen el **35 %** de la nota final.

### 🟨 Fase B — Generador de Prompts Automático
- El botón **🎲 Asignar escenario** sortea un reto ético/práctico.
- **Los 4 integrantes** redactan **UN** prompt perfecto en la caja de texto.
- El panel derecho te da **feedback en vivo** con la checklist de ingeniería
  de prompts (rol, contexto, restricciones, formato, audiencia, tono…).
- Vale el **65 %** de la nota final.

### 🟩 Fase C — Calificación Final y Constancia
- El dashboard combina teoría + estructura del prompt → **nota sobre 100**.
- Genera tu **constancia descargable** con el nombre del equipo, integrantes,
  el escenario y el prompt redactado.
- **Descarga la constancia** y súbela a tu `ENTREGA.md` (link o captura).

## 3. Reparto sugerido de roles (equipo de 4)

Para que nadie se quede sin aportar su parte del prompt:

| Integrante | Se encarga de… |
|------------|----------------|
| A | **Rol**: definir quién es la IA ("actúa como…"). |
| B | **Contexto**: explicar situación, tema y datos clave. |
| C | **Restricciones**: qué NO debe hacer, límites, tono. |
| D | **Formato + cierre**: cómo quieres la salida y revisar el prompt completo. |

## 4. Entregables (qué subir a GitHub)

1. `semana-02/ENTREGA.md` con:
   - **Equipo** y **4 integrantes** con su rol de la tabla de arriba.
   - La **nota final** y el **desglose** (teoría vs. prompt).
   - El **prompt** que redactaron (cópialo tal cual).
   - Una **reflexión de 3 líneas**: ¿qué elemento del prompt cambió más el
     resultado y por qué?
2. La **constancia descargada** (imagen o `.txt`) dentro de `semana-02/`.
3. Captura de la Fase A aprobada (evidencia de la teoría).

### Plantilla para `ENTREGA.md`

```markdown
# Prompt Battle — Equipo #N

| Integrante | Rol en el prompt |
|------------|------------------|
| ... | Rol |

## Nota final: __/100
- Fase A (teoría): __/10
- Fase B (prompt): __/10

## Escenario sorteado
...

## Nuestro prompt
> (pegar aquí)

## Reflexión
...
```

## 5. Rúbrica (20 puntos)

| Criterio | Puntos |
|----------|--------|
| Fase A: respuestas correctas de teoría | 5 |
| Fase B: el prompt incluye rol + contexto + restricciones | 8 |
| Fase B: calidad/creatividad y elementos avanzados | 4 |
| Constancia + `ENTREGA.md` completos | 3 |

## 6. Autochequeo del equipo ✅

- [ ] Entiendo qué es un **token** con un ejemplo propio.
- [ ] Puedo explicar por qué la IA **alucina**.
- [ ] Sé qué es un **sesgo** y de dónde viene.
- [ ] Mi prompt tiene **rol, contexto y restricciones** (y lo comprobó el panel).
- [ ] Descargué la **constancia** y está en la carpeta.
- [ ] `ENTREGA.md` subido en la rama `equipo-N-semana-02`.

> 🧪 **Reto extra (opcional):** cambien UNA palabra del prompt (por ejemplo, el
> rol) y comparen la respuesta de la IA. ¿Cuánto cambió? Anótenlo en la reflexión.