import cv2
import time
import numpy as np

# Para salvar o resultado em um arquivo chamado output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Iniciando a webcam
cap = cv2.VideoCapture(0)

# Permitindo que a webcam inicie fazendo o código aguardar 2 segundos
time.sleep(2)
bg = 0

# Capturando o plano de fundo durante 60 quadros
for i in range(60):
    ret, bg = cap.read()
# Invertendo o plano de fundo
bg = np.flip(bg, axis=1)

# Lendo o quadro capturado até que a câmera esteja aberta
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    # Invertendo a imagem por motivo de consistência
    img = np.flip(img, axis=1)

    # Convertendo a cor de BGR para HSV

    # Gerando máscara para detectar a cor vermelha (os valores podem ser alterados)

    # Abrindo e expandindo a imagem onde há a máscara 1 (cor)

    # Selecionando apenas a parte que não possui máscara 1 e salvando-a na máscara 2

    # Mantendo apenas a parte das imagens sem a cor vermelha
    # (ou qualquer outra cor que você escolher)

    # Mantendo apenas a parte das imagens com a cor vermelha

    # Gerando o resultado final
    final_output = img
    output_file.write(img)
    # Exibindo o resultado para o usuário
    cv2.imshow("magica", final_output)
    cv2.waitKey(1)


cap.release()
out.release()
cv2.destroyAllWindows()
