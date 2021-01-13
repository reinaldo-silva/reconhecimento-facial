import cv2

carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('fotos/image5.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemCinza)

for(x , y, l, a) in faces:
    imagemCorte = cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)
    localOlho = imagem[y:y + a, x:x + l]
    localOlhoCinza =cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detectado = carregaOlho.detectMultiScale(localOlhoCinza, scaleFactor=1.3, minNeighbors=9)

    for(ox, oy, ol, oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

cv2.imshow("Detecta face e os olhos", imagem)
cv2.waitKey()