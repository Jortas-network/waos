import cv2

def aplicar(imagen):
    #Aplica el filtro laplaciano a la imagen (Utiliza la mascara -1,4)
    laplaciano = cv2.Laplacian(imagen, cv2.CV_64F,ksize=1)
    #Retorna la imagen aplicada el filtro, corrigiendo los valores negativos
    return cv2.convertScaleAbs(laplaciano)

# La segunda derivada de una función f(x) es f''(x).
# En imágenes (funciones discretas), se aproxima usando diferencias finitas:
# f''(x) ≈ f(x+1) - 2*f(x) + f(x-1)

# En 2D (para imágenes), el operador laplaciano es:
# ∇²f(x, y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4*f(x, y)

# Esto se representa como un kernel de convolución:
#     0  1  0
#     1 -4  1
#     0  1  0