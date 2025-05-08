import cv2
import numpy as np

def aplicar(imagen):
    """Aplicamos filtro laplaciano (-1,8)"""
    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],dtype=np.float32)
    resultado = cv2.filter2D(imagen,-1,kernel)
    return cv2.convertScaleAbs(resultado)