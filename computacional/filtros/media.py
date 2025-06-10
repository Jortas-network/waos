import cv2
import numpy as np

def aplicar(image):
    """Aplica filtro de media 1/9"""
    kernel = np.ones((3,3),dtype=np.float32)/9
    return cv2.filter2D(image, -1, kernel)
