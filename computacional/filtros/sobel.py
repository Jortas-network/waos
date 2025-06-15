import cv2

def aplicar(imagen):
    #Aplica filtro de Sobel combinado
    #Saca las gradientes de x y y a la imagen
    sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    #Combia las gradientes sacando la magnitud
    combinado = cv2.magnitude(sobelx, sobely)
    #retorna la imagen con filtro de sobel con valores positivos
    return cv2.convertScaleAbs(combinado)
