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

## Preguntas abiertas
1. ¿Carta y gesto se muestran a la vez o por separado?
2. ¿Cómo se confirma la jugada? (mantener X segundos, tecla, etc.)
3. ¿El oponente se dibuja por capas (cuerpo/cara + mano con carta + mano con gesto) para no dibujar 25 combinaciones? (Propuesta de Claude: sí, por capas.)
4. ¿Imágenes fijas o animaciones (parpadeo, movimiento al pensar)?
5. ¿Quién dibuja el pixel art y con qué programa? Claude no puede dibujar pixel art de calidad; recomendado que lo haga Alberto con Aseprite / Piskel / LibreSprite, y Claude prepara lista de piezas, tamaños y lo integra. ¿Formato y tamaño del modelo actual?
6. ¿Se muestra la imagen de la webcam en pantalla (ventanita para ver si se reconoce bien)?
7. ¿Lenguaje/herramienta del juego? (Propuesta de Claude: Python + Pygame, todo junto con OpenCV.) ¿Alguna exigencia del profesor?

## Decisiones tomadas
- Cartas de diseño propio, muy distintivas.
- Grupo y fecha de entrega: no relevantes para el scope.

## Avances
- Sesión 1 (scope): lectura del repositorio, definición del objetivo general y del apartado videojuego. En curso.
