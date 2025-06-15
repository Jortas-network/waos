import cv2
import numpy as np

def aplicar(imagen):
    #Aplica filtro de media 1/16
    kernel_16 = np.array([[1,2,1],[2,4,2],[1,2,1]],dtype=np.float32) / 16
    #Retorna la imagen aplicada el filtro
    return cv2.filter2D(imagen, -1, kernel_16)

# El filtro de media (promedio) suaviza la imagen reduciendo el ruido.
# Para cada píxel, se toma el promedio de los valores de sus vecinos.

# En 1D, para una función f(x):
# media ≈ (f(x-1) + f(x) + f(x+1)) / 3

# Un filtro de media estándar 3x3 usa 1/9 en cada posición.
# Si usas 1/16, el kernel sería:
#     1/16  1/16  1/16
#     1/16  1/16  1/16
#     1/16  1/16  1/16
# Esto suaviza la imagen, pero el resultado será más oscuro porque la suma total es 9/16 < 1.
