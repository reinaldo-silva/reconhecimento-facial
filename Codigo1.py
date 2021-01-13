import cv2

carregaAlgoritimo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('fotos/image2.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritimo.detectMultiScale(imagemCinza, scaleFactor=1.08, minNeighbors=3, minSize=(50, 50))

print(faces)

for(x , y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)

cv2.imshow("Faces", imagem)
cv2.waitKey()