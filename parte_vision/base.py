import cv2 as cv
import mediapipe as mp # la libreria de google para detectar manos
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Cargamos el modelo (hay que descargar gesture_recognizer.task)
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

cap = cv.VideoCapture(0) # abrir la camara

# nombres de los gestos en nuesttro juego
nombres = {
    "Closed_Fist": "Atacar (puno)",
    "Open_Palm": "Defender (palma)",
    "Thumb_Up": "Curarse (pulgar arriba)",
    "ILoveYou": "Huir (te quiero)",
    "Pointing_Up": "Cargar (indice arriba)",
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1) # modo espejo paar vernos bien

    # MediaPipe necesita RGB, y OpenCV trabaja en BGR
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb) # convertir la imagen a mediapipe

    result = recognizer.recognize(mp_image) # el modelo busca la mano, sus 21 puntos y el gesto

    h, w = frame.shape[:2] # guarda el alto (h) y ancho (w) de la imagen en píxeles

    if result.hand_landmarks:
        # Dibujar los 21 puntos de cada mano detectada
        for mano in result.hand_landmarks:
            for punto in mano:
                x, y = int(punto.x * w), int(punto.y * h)
                cv.circle(frame, (x, y), 5, (0, 0, 255), -1)

        # coge el nombre del gesto detectado y lo traduce a nuestro juego, si no esta pone gesto no valido
        gesto = nombres.get(result.gestures[0][0].category_name, "Gesto no valido")        
        score = result.gestures[0][0].score
        texto = f"{gesto} ({score:.2f})"
    else:
        texto = "No veo mano" # si no detecta mano

    cv.putText(frame, texto, (20, 50), cv.FONT_HERSHEY_SIMPLEX,
               1.2, (0, 255, 0), 2)

    cv.imshow('Gestos', frame)

    if cv.waitKey(1) & 0xFF == ord('q'): # poner q para cerrar
        break

cap.release()
cv.destroyAllWindows()