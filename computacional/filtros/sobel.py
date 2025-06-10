import cv2

def aplicar(imagen):
    """Aplica filtro de Sobel combinado"""
    sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    combined = cv2.magnitude(sobelx, sobely)
    return cv2.convertScaleAbs(combined)
