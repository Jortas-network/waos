import cv2
import numpy as np

def aplicar(imagen):
    """Aplica filtro de media 1/16"""
    kernel_16 = np.array([[1,2,1],[2,4,2],[1,2,1]],dtype=np.float32) / 16
    return cv2.filter2D(imagen, -1, kernel_16)
