import cv2

def apply(image, ksize=3):
    """Aplica filtro de mediana"""
    return cv2.medianBlur(image, ksize)
