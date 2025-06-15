import cv2
import numpy as np

def aplicar(imagen):
    #Filtro laplaciano (-1 y 8)
    #Se crea la mascara kernel del laplaciano
    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],dtype=np.float32)
    #Al resultado se le aplica el filtro con la mascara
    resultado = cv2.filter2D(imagen,-1,kernel)
    #se retorna el resultado en numeros absolutos
    return cv2.convertScaleAbs(resultado)