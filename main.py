import cv2 as cv2

# Criando conexão com a webcam
webcam = cv2.VideoCapture(0)

# Se a webcam estiver aberta
if webcam.isOpened():
    # leia
    validação, frame = webcam.read()
    # Para apresentar
    while validação:
        # Faça a leitura a toda hora
        validação, frame = webcam.read()
        # Nome da janela
        cv2.imshow("WebCam", frame)
        # Limitando o fps e lendo uma tecla que será clicada
        key = cv2.waitKey(60)
        # Se a tecla for ESC
        if key == 27: #ESC
            # Quebre o loop
            break
    # Registre um frame, com o nome de foto.png
    cv2.imwrite("Foto.png", frame)

# Quando tudo terminar feche a câmara e termine a ligação
webcam.release()
cv2.destroyAllWindows()