import cv2
import mediapipe as mp

#Inicializar o openCV e o mediapipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_de_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break

    #Reconhecer os rostos
    lista_rostos = reconhecedor_de_rostos.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #Desenhar os rostos
            desenho.draw_detection(frame, rosto)

    cv2.imshow("Rostos na webcam", frame)

    #Quando apertar Esc (código 27), para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()