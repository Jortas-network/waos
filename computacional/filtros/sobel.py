import cv2

def aplicar(imagen):
    #Aplica filtro de Sobel combinado
    #Saca las gradientes de x y y a la imagen
    sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    #Combia las gradientes sacando la magnitud
    combinado = cv2.magnitude(sobelx, sobely)
    #retorna la imagen con filtro de sobel con valores positivos
    return cv2.convertScaleAbs(combinado)

# El filtro de Sobel es un operador para detectar bordes en imágenes.
# Calcula una aproximación de la derivada (gradiente) en dirección horizontal (x) y vertical (y).

# Los kernels de Sobel más comunes son:
# Para detectar bordes horizontales (Sobel X):
#   -1  0  1
#   -2  0  2
#   -1  0  1

# Para detectar bordes verticales (Sobel Y):
#    1  2  1
#    0  0  0
#   -1 -2 -1

# Combina las gradientes sacando la magnitud:
# La magnitud del gradiente se calcula así:
#     magnitud = sqrt(sobelx**2 + sobely**2)
# Esto resalta los bordes sin importar la dirección.

# Convierte la imagen resultante a valores positivos de 8 bits:
# cv2.convertScaleAbs toma los valores flotantes (que pueden ser negativos)
# y los convierte a enteros sin signo (0-255), listos para mostrar como imagen.