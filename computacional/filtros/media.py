import cv2
import numpy as np

def aplicar(image):
    #Aplica filtro de media 1/9
    kernel = np.ones((3,3),dtype=np.float32)/9
    return cv2.filter2D(image, -1, kernel)

# El filtro de media (promedio) suaviza la imagen reduciendo el ruido.
# Para cada píxel, se toma el promedio de los valores de sus vecinos.

# En 1D, para una función f(x):
# media ≈ (f(x-1) + f(x) + f(x+1)) / 3

# En 2D (imágenes), el kernel de convolución más común es de 3x3:
#     1/9  1/9  1/9
#     1/9  1/9  1/9
#     1/9  1/9  1/9