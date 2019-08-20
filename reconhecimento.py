import cv2 #importa a bibilioteca opencv
from random import randint #importa a bibilioteca para gerar números randômicos

#método transparentOverlay serve para deixar a imgem importada trasparente
def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    #função overlay deixa a imagem em png trasparente
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][2] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src

winName = 'Janela de Teste para o SOPT'

cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#importa a webcamq
video = cv2.VideoCapture(2)

#faz a webcam funcionar a 30fps
#video.set(cv2.CAP_PROP_FPS, 30)

#chama o classificador para deteção de faces
classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
#importa o primeiro emoj
imagem = cv2.imread('emoji/1.png')
#contador para trocar os emojs quando a quantidade de faces mudar
contador = 0

#laço de repetição para o programa funcionar infinitamente, o software só desliga quando apertar a letra q
while True:
    #as variável conectado retorna um boolean que informa o estado da conexão, e o frame retorna
    #o video capturado pela webcam
    conectado, frame = video.read()
    #img_gray transforma o vídeo em escala de cinza para facilitar na deteçao
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #faces_detectadas representa a região onde as faces foram encontradas
    faces_detectadas = classificador.detectMultiScale(img_gray, minNeighbors=10, scaleFactor=1.1, maxSize=(256,256))

    #o laço for é usado para percorer a região com as faces detectadaq
    for (x, y, a, l) in faces_detectadas:
        x += -20
        y += -20
        a += 20
        l += 20
        # img_capturada retorna a região desenhada da face encontrada
        img_capturada = cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
        # o if testa se há novas faces, se sim o emoj muda
        if (len(faces_detectadas) != contador):
            # randint sorteia um número entre 1 e 9, esses números representa o nome do arquivo onde está os emoji
            imagem = cv2.imread('emoji/{}.png'.format(str(randint(1, 75))))
            # retorna o número de faces encontradas para variável contador
            contador = (len(faces_detectadas))
        # scale_precent representa a altura _ largura do emoji, os valores são alteerados de acordo com o tamanho da face
        scale_percent = (a + l) / 10
        # largura da face capturada pelo obturador
        width = int(img_capturada.shape[1] * scale_percent / 120)
        # altura da face capturada pelo obturador
        height = int(img_capturada.shape[0] * scale_percent / 90)
        # tupla para armazenar os valores de largura e altura
        dim = (width, height)

        # reigão da área total onde se encontra a face
        regiao = img_capturada[y: y + a, x: x + l]
        # funcao resize permite importar uma nova imagem dento da mesma janela
        resized = cv2.resize(imagem, dim, interpolation=cv2.INTER_AREA)

        # chamada da função para deixar a imagem trasparente
        transparentOverlay(regiao, resized)

    cv2.putText(frame, 'By: Otavio Rocha Faria, SI/8P', (0,30), cv2.FONT_ITALIC, (1.2), (0,0,255), 2)

    #função que chama a janela para visualização
    cv2.imshow(winName, frame)
    #condição permite parar o laço se o usuário apertar q
    if cv2.waitKey(1) == ord('q'):
        break

#video relise serve para limpar o buffer o opencv
video.release()
#descontroi todas as janelas existentes
cv2.destroyAllWindows()