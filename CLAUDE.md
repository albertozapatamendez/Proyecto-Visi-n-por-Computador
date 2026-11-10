Estudiante universitario, principiante con IA y Claude Code. Responder siempre en español.

## Reglas de trabajo
1. Preguntar todas las ambigüedades antes de actuar por mi cuenta.
2. No inventar nada. Si no sé cómo hacer algo, preguntar.
3. Usar el mínimo de tokens posible: respuestas cortas, sin trabajo extra.
4. Avisar y preguntar antes de tareas costosas (renderizar, mucho razonamiento, investigación larga).
5. Corregir sin miedo y proponer la mejor opción, aunque implique otra app o herramienta.
6. En todas las respuestas llamame por mi nombre, por ejemplo: "Alberto, ...."

Hay que ampliar este CLAUDE.md para utilizarlo durante todo el proyecto, definiendo objetivos, actualizando avances y recopilando el trabajo hecho.

---

# Proyecto: juego "Elementos y Acciones" controlado por webcam

## Objetivo general
Juego por turnos contra la máquina, en tiempo real con webcam. Reglas completas en `reglas_juego.pdf`.
El jugador elige su jugada mediante visión por computador:
- **Elemento** (5): mostrando una carta impresa. Cartas de diseño propio, con color y símbolo muy distintivos para facilitar el reconocimiento.
- **Acción** (5): haciendo un gesto con la mano (ver tabla de gestos en el apartado de visión).

El proyecto se divide en dos grandes apartados: **videojuego** y **visión por computador**.

## Requisitos de la asignatura (de `Instrucciones proyecto Visión por Computador.md`)
- **Entregables:** memoria del proyecto + exposición oral en clase de prácticas. Guardar resultados y capturas desde el principio.
- **Datos:** hay que crear base de datos propia (cartas y gestos son nuestros): fotos/vídeos de cartas y gestos, cada uno etiquetado. El profesor avisa de que esto es más complicado. Para gestos puede ayudar una herramienta existente de detección de mano (a decidir).
- **Técnicas:** el profesor recomienda la metodología y asesora. Preguntarle pronto si permite herramientas ya hechas o prefiere técnicas vistas en clase.
- **Evaluación (lo más importante):** no importa tanto acertar mucho como evaluar bien: % de acierto con imágenes no usadas para entrenar, qué cartas/gestos se confunden entre sí (matriz de confusión), pruebas con distinta luz y distintas personas. La nota depende sobre todo de la visión y su evaluación, no del juego.

## Apartado 1: Videojuego
- La máquina elige elemento y acción al azar (ver reglas).
- Interfaz: vista en primera persona (POV) de un jugador sentado a una mesa (casino/posada/escenario).
  - Franja inferior de la pantalla: la mesa.
  - Al otro lado, de frente, el personaje oponente en pixel art (Alberto ya tiene el modelo base).
  - Fondo fijo (por decidir).
- Estados del oponente a crear:
  - Enseñando cada una de las 5 cartas.
  - Haciendo cada una de las 5 acciones.
  - Estados de ánimo variados: pensando, enfadado, alegre, aburrido, etc.
- Se dedicará una sesión entera a crear los estados del pixel art y el fondo. En esa sesión se deciden también el fondo y el formato/tamaño del modelo. El `.md` resultado de esa sesión se subirá al repo.
- **Oponente por capas:** pose base + capa de mano con carta + capa de mano con gesto (sin repetir combinaciones).
- **Poses extra:** 1 o 2 poses base modestas (p. ej. esperando a que el jugador elija, inicio/fin de partida).
- **Animaciones:** muy modestas, si no cuestan mucho. Se decide al programar; si cuestan mucho, se prescinde.
- **Webcam en pantalla:** sí, en una ventanita, para que el jugador vea si se le reconoce.

### Objetivo de gráficos (fijado en sesión 1)
- **Fondo:** fijo. Puede haber 1–2 fondos distintos (solo estéticos, p. ej. uno al azar por partida).
- **Oponente:**
  - **2–3 poses de espera** (sin capas de manos): esperando (manos no visibles), mano en la mesa, manos detrás de la cabeza…
  - **1 pose de acción** por capas: cuerpo base + mano 1 con una de las 5 cartas + mano 2 con uno de los 5 gestos.
  - **Cara:** capa aparte con varias emociones, común a todas las poses.
- **Piezas a dibujar (aprox.):** 3–4 poses de cuerpo, 5 manos con carta, 5 manos con gesto, 4–6 caras, 1–2 fondos.
- **Reglas de dibujo para que encaje:**
  1. Todas las piezas al mismo tamaño de lienzo y alineadas (cada capa se coloca encima sin ajustar).
  2. La cabeza en la misma posición en todas las poses (si cambia, caras propias para esa pose o desplazarlas por código).
- **Animaciones modestas:** respirar (por código), parpadeo (dibujado, 2–3 frames), mover la carta al sacarla (por código).

## Apartado 2: Visión por computador
- Reconocer por webcam la carta (elemento) y el gesto (acción) del jugador.
- **Lógica de detección:** da igual el orden, la mano o si es simultáneo. El programa solo comprueba: ¿carta detectada? sí/no; ¿gesto detectado? sí/no. Cuando tiene ambos, se resuelve el turno.
- **Gestos:** fijos (posturas de mano, sin movimiento). Definidos:
  | Acción | Gesto |
  |---|---|
  | Atacar | Puño cerrado |
  | Defender | Palma abierta |
  | Curarse | Pulgar hacia arriba |
  | Huir | Dedos en V |
  | Cargar | Índice arriba |
  - Posibles confusiones a vigilar en la evaluación: puño ↔ pulgar arriba (solo cambia el pulgar) e índice arriba ↔ V (solo cambia un dedo).
- **Hardware:** webcam del portátil o el móvil como webcam (p. ej. apps tipo DroidCam/Iriun). Gráfica AMD Radeon (sin CUDA): si se entrena una red, hacerlo en CPU o con modelos ligeros.
- **Pendientes de visión:**
  - Técnicas: en clase se ha visto segmentación y contornos. MediaPipe (puntos de la mano) está permitido.
  - Diseño de las cartas (colores y símbolos): se decide junto con Claude.
  - Estabilidad: que solo cuente una detección si se mantiene ~1 s (decidir al programar).
  - Base de datos: quién aparece (solo Alberto o varias personas), fondos y luces (decidir al programar).
  - Cómo se hace el código y la base de datos de cartas y gestos.

## Investigación (sesión 1) y propuesta técnica
Propuesta de Claude, pendiente de depurar con Alberto.

### Animaciones y capas (Pygame)
- **Animación = secuencia de frames.** Se guardan en un *sprite sheet* (una imagen con todos los frames) y el juego cambia de frame cada X ms. Método estándar, con tutoriales sencillos.
- **Capas = dibujar en orden:** fondo → oponente → manos → mesa → interfaz. Pygame lo hace sin herramientas especiales (también tiene grupos de sprites por capas).
- **Animaciones por código (sin dibujar más frames):** mover 1–2 px arriba/abajo ("respirar"), desplazar la carta al sacarla, temblor al enfadarse. Coste muy bajo. Encaja con "animaciones modestas". (Técnica conocida por Claude, no sacada de una fuente.)
- **Animaciones dibujadas:** solo pequeñas (p. ej. parpadeo de 2–3 frames). Las de gestos completos frame a frame cuestan más (sobre todo de dibujo).
- **Aseprite** exporta cada capa por separado (CLI `--split-layers`/`{layer}`, `{tag}`, `{frame}`; formato JSON array). No hay ejemplo de carga en Pygame, pero el código es corto.

### Proyectos parecidos
- Muchos proyectos de **piedra-papel-tijera con webcam + MediaPipe** contra la máquina (= nuestra parte de gestos).
- Idea útil: categoría **"lectura falsa / ningún gesto válido"**.
- No se encontró ninguno que combine MediaPipe con una interfaz completa en Pygame: aportación propia del proyecto.

### Gestos (MediaPipe: 21 puntos de la mano)
| Opción | Cómo | Valoración |
|---|---|---|
| A. Reglas a mano | "si índice estirado y resto doblados → pistola" | Rápido, pero frágil y poco evaluable |
| B. **Puntos + clasificador propio** | Guardar los 21 puntos de muchas fotos por gesto y entrenar un clasificador sencillo (scikit-learn: SVM / Random Forest) | **Recomendada.** CPU, sin GPU. Genera base de datos propia y evaluación (% acierto, matriz de confusión) |
| C. Gesture Recognizer de Google reentrenado | Herramienta oficial con gestos nuevos | Más "caja negra", menos trabajo propio visible |

### Cartas
- Método habitual: 1) **encontrar el contorno** de la carta; 2) **enderezarla** (corrección de perspectiva); 3) **identificarla** con plantillas (*template matching*, algo rígido) o por color dominante + forma del símbolo.
- Ventaja: las cartas son de diseño propio → 5 colores muy distintos + un símbolo cada una → basta **segmentación por color + contornos** (lo visto en clase). Evaluable por separado.
- Riesgo: piel o ropa pueden confundir el color → probar con distintas luces y fondos.
- Alternativa descartada como método principal: marcadores **ArUco** impresos (OpenCV los reconoce casi perfecto, pero quita mérito de visión).

### Recomendación global
- **Juego:** Pygame, oponente por capas, animaciones por código (respirar, mover carta) + algún parpadeo dibujado si da tiempo.
- **Gestos:** MediaPipe + clasificador entrenado con nuestros datos (opción B).
- **Cartas:** contornos + segmentación por color, con cartas diseñadas para facilitarlo.
- **Evaluación:** separada para gestos y cartas: % acierto, matriz de confusión, pruebas con varias luces y personas.

### Fuentes
- Animación Pygame: https://pythonprogramming.altervista.org/sprite-animation-with-sprite-sheets/ · https://www.101computing.net/?p=22126 · https://gurubase.io/g/python/implementing-multiple-animations-in-pygame · https://gamedevacademy.org/pygame-sprite-tutorial-complete-guide/
- Aseprite: https://www.aseprite.org/cli/ · https://community.aseprite.org/t/export-each-layer-of-a-file-in-a-different-sprite-sheet/2876 · https://mintlify.com/aseprite/aseprite/features/sprite-sheets
- Gestos MediaPipe: https://developers.google.com/edge/mediapipe/solutions/vision/gesture_recognizer/python · https://instructables.com/How-to-Train-Custom-Hand-Gestures-Using-Mediapipe
- Piedra-papel-tijera: https://github.com/freestyleabg/computer-vision-rock-paper-scissors · https://yashd-dev.vercel.app/posts/post1-rps · https://www.instructables.com/Rock-Paper-Scissors-With-Open-CV · https://awesome.ecosyste.ms/projects/github.com%2Fjakub-nowicki%2Frock-paper-scissors
- Cartas: https://forum.opencv.org/t/using-template-matching-to-identify-playing-cards/3390 · https://forum.opencv.org/t/recognizing-playing-cards/17403 · https://www.preprints.org/manuscript/202301.0030

## Logística (TEMPORAL, pendiente de confirmar)
"Decisión provisional: Alberto aún tiene que valorar si hace una partición de Linux."
- **Dónde programar:** Windows directamente. VirtualBox descartado (mal acceso a la webcam y poca potencia). Partición Linux: no necesaria, pero pendiente de decidir.
- **Herramientas:** VS Code + Python + entorno virtual (venv). En clase se usa Python + OpenCV.
- **Repositorio:** el código vive en este repo de GitHub; se clona en el PC y se trabaja ahí.
- **Qué es el juego:** un programa Python local, sin internet ni servidor. Sin motor gráfico (nada de Unity/Godot): se usa la librería **Pygame** para la ventana y el dibujo.
- **Llevarlo a otro PC:** copiar el proyecto e instalar librerías, o empaquetarlo en `.exe` con PyInstaller. Móvil/web fuera del alcance.
- **Cómo se junta visión y juego:** todo en un mismo programa, en bucle:
  1. OpenCV captura un fotograma de la webcam.
  2. Módulo de visión: detecta carta y gesto.
  3. Lógica del juego: aplica reglas (aciertos, vidas, puntos).
  4. Pygame dibuja la pantalla (fondo, mesa, oponente y quizá ventanita de webcam).
- **Estructura del código (propuesta):** archivos separados para visión, lógica e interfaz, para hacerlos y probarlos en sesiones distintas.

## Preguntas abiertas
1. ¿Partición con Linux o Windows? (Ver "Logística (TEMPORAL)"; Alberto lo está pensando. Recomendación de Claude: Windows.)
2. Formato y tamaño del pixel art, y fondo: se deciden en la sesión de pixel art.
3. Animaciones: cuáles y cuántas, según lo que cueste programarlas.
4. El diseño de las cartas.

## Decisiones tomadas
- Cartas de diseño propio, muy distintivas.
- La jugada se confirma sola al detectar carta y gesto (orden indiferente).
- Gestos fijos: atacar = puño, defender = palma, curarse = pulgar arriba, huir = V, cargar = índice arriba.
- Gráficos: ver "Objetivo de gráficos" (2–3 poses de espera + 1 pose de acción por capas + cara por capas + 1–2 fondos fijos).
- Webcam visible en pantalla en una ventanita.
- MediaPipe permitido.
- Pixel art: lo dibuja Alberto a partir de su modelo ya hecho (solo faltan los estados). Claude prepara la lista de piezas y lo integra en el juego.
- Grupo y fecha de entrega: no relevantes para el scope.

## Avances
- Sesión 1 (scope): lectura del repositorio, objetivo general, apartados videojuego y visión, logística, requisitos de la asignatura e investigación técnica. En curso (falta dividir el trabajo en bloques).
