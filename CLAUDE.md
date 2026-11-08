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
- **Acción** (5): haciendo un gesto con la mano (gestos aún sin definir; ejemplo: atacar = mano en forma de pistola).

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
- Se dedicará una sesión entera a crear los estados del pixel art y el fondo.

## Apartado 2: Visión por computador
- Reconocer por webcam la carta (elemento) y el gesto (acción) del jugador.
- (Pendiente de detallar por Alberto.)

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
1. ¿Carta y gesto se muestran a la vez o por separado?
2. ¿Cómo se confirma la jugada? (mantener X segundos, tecla, etc.)
3. ¿El oponente se dibuja por capas (cuerpo/cara + mano con carta + mano con gesto) para no dibujar 25 combinaciones? (Propuesta de Claude: sí, por capas.)
4. ¿Imágenes fijas o animaciones (parpadeo, movimiento al pensar)?
5. ¿Formato y tamaño (resolución) del modelo de pixel art?
6. ¿Se muestra la imagen de la webcam en pantalla (ventanita para ver si se reconoce bien)?
7. ¿Partición con Linux o Windows? (Ver "Logística (TEMPORAL)"; pendiente de que Alberto decida.)
8. Preguntar al profesor: ¿se pueden usar herramientas/modelos ya hechos o hay que usar técnicas vistas en clase?

## Decisiones tomadas
- Cartas de diseño propio, muy distintivas.
- Pixel art: lo dibuja Alberto a partir de su modelo ya hecho (solo faltan los estados). Claude prepara la lista de piezas y lo integra en el juego.
- Grupo y fecha de entrega: no relevantes para el scope.

## Avances
- Sesión 1 (scope): lectura del repositorio, definición del objetivo general y del apartado videojuego. En curso.
