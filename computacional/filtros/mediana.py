import cv2

def aplicar(image):
    """Aplica filtro de mediana"""
    return cv2.medianBlur(image, 3)
