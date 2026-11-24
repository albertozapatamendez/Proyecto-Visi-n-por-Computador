import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os, csv, time
 
# ajustes de la captura
MUESTRAS = 100 # muestras por gesto y ronda
DURACION = 20 # segundos que dura la captura
INTERVALO = DURACION / MUESTRAS # segundos entre muestras (0.2 s)
 
# datos de esta sesion (para saber luego quien y con que luz)
persona = input("Nombre de la persona: ")
luz = input("Luz (ej: natural, artificial, baja): ")
 
# etiquetas por tecla y gesto
etiquetas = {
    ord('1'): "puno", ord('2'): "palma", ord('3'): "pulgar",
    ord('4'): "tequiero", ord('5'): "indice", ord('0'): "ninguno",
}
 
# carpetas y CSV
os.makedirs("dataset/fotos", exist_ok=True)
csv_path = "dataset/puntos.csv"
nuevo = not os.path.exists(csv_path)
f = open(csv_path, "a", newline="")
writer = csv.writer(f)
if nuevo:
    cabecera = ["gesto", "persona", "luz", "foto"]
    cabecera += [f"{c}{i}" for i in range(21) for c in ("x", "y", "z")]
    writer.writerow(cabecera)
 
# Modelo (solo para ver los puntos y comprobar que detecta la mano)
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)
 
cap = cv.VideoCapture(0)
contador = {}
 
# Estado de la captura automática
capturando = False
gesto_actual = None
guardadas = 0
inicio = 0
ultima = 0
 
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.flip(frame, 1)
    limpio = frame.copy()  # copia sin dibujos, es la que se guarda
 
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = recognizer.recognize(mp_image)
 
    h, w = frame.shape[:2]
    if result.hand_landmarks:
        for punto in result.hand_landmarks[0]:
            cv.circle(frame, (int(punto.x * w), int(punto.y * h)), 5, (0, 0, 255), -1)
 
    ahora = time.time()
 
    # Guardar una muestra cada INTERVALO segundos mientras dura la captura
    if capturando and ahora - ultima >= INTERVALO:
        ultima = ahora
        if result.hand_landmarks or gesto_actual == "ninguno":
            nombre = f"{gesto_actual}_{persona}_{luz}_{int(ahora*1000)}.jpg"
            cv.imwrite(f"dataset/fotos/{nombre}", limpio)
            fila = [gesto_actual, persona, luz, nombre]
            if result.hand_landmarks:
                for p in result.hand_landmarks[0]:
                    fila += [p.x, p.y, p.z]
            else:
                fila += [""] * 63
            writer.writerow(fila)
            f.flush()
            guardadas += 1
            contador[gesto_actual] = contador.get(gesto_actual, 0) + 1
        # Si no hay mano, esa muestra se salta (no cuenta)
 
        if guardadas >= MUESTRAS:
            capturando = False
            print(f"Terminado: {guardadas} muestras de {gesto_actual}")
 
    # Textos en pantalla
    cv.putText(frame, f"{persona} | {luz}", (20, 30),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv.putText(frame, str(contador), (20, 60),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    if capturando:
        cv.putText(frame, f"GRABANDO {gesto_actual}: {guardadas}/{MUESTRAS} ({int(ahora - inicio)}s)",
                   (20, 90), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv.imshow('Recoger datos', frame)
 
    tecla = cv.waitKey(1) & 0xFF
    if tecla == ord('q'):
        break
    # Pulsar una tecla de gesto inicia la captura (si no hay otra en curso)
    if tecla in etiquetas and not capturando:
        gesto_actual = etiquetas[tecla]
        capturando = True
        guardadas = 0
        inicio = ahora
        ultima = 0
        print(f"Capturando {gesto_actual}...")
 
f.close()
cap.release()
cv.destroyAllWindows()