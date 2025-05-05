import cv2

def apply(image):
    """Aplica filtro de Sobel combinado"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    combined = cv2.magnitude(sobelx, sobely)
    return cv2.convertScaleAbs(combined)
