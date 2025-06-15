import cv2

def aplicar(image):
    #Aplica filtro de mediana y la retorna
    return cv2.medianBlur(image, 3)

# El filtro de mediana es un filtro no lineal que reemplaza cada píxel
# por la mediana de los valores de sus vecinos en una ventana (por ejemplo, 3x3).
# Es muy útil para eliminar ruido tipo "sal y pimienta" sin difuminar los bordes.

# Ejemplo: para una ventana 3x3 alrededor de un píxel:
# [  5,  80,  7 ]
# [  6, 255,  8 ]
# [  4,   9,  6 ]
# Ordenamos los valores: [4, 5, 6, 6, 7, 8, 9, 80, 255]
# La mediana es 7, así que el píxel central se reemplaza por 7.
 
