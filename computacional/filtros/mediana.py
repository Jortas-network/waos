import cv2

def aplicar(image):
    #Aplica filtro de mediana y la retorna
    return cv2.medianBlur(image, 3)
