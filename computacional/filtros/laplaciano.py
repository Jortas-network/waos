import cv2

def aplicar(imagen):
    """Aplica filtro Laplaciano"""
    laplaciano = cv2.Laplacian(imagen, cv2.CV_64F)
    return cv2.convertScaleAbs(laplaciano)
