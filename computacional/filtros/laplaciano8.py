import cv2
import numpy as np

def aplicar(imagen):
    #Filtro laplaciano (-1 y 8)
    #Se crea la mascara kernel del laplaciano
    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],dtype=np.float32)
    #Al resultado se le aplica el filtro con la mascara
    resultado = cv2.filter2D(imagen,-1,kernel)
    #se retorna el resultado en numeros absolutos
    return cv2.convertScaleAbs(resultado)

# La segunda derivada de una función f(x) es f''(x).
# En imágenes (funciones discretas), se aproxima usando diferencias finitas:
# f''(x) ≈ f(x+1) - 2*f(x) + f(x-1)

# En 2D (para imágenes), el operador laplaciano es:
# ∇²f(x, y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4*f(x, y)
# O una variante más común:
#     1  1  1
#     1 -8  1
#     1  1  1