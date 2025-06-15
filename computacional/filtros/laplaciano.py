import cv2

def aplicar(imagen):
    #Aplica el filtro laplaciano a la imagen (Utiliza la mascara -1,4)
    laplaciano = cv2.Laplacian(imagen, cv2.CV_64F,ksize=1)
    #Retorna la imagen aplicada el filtro, corrigiendo los valores negativos
    return cv2.convertScaleAbs(laplaciano)
