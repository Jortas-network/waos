import cv2
import numpy as np

def cargar_imagen(ruta):
    #Carga la imagen y la retorna
    imagen = cv2.imread(ruta)
    return imagen

def cargar_imagen_gris(imagen_original):
    #Separamos los 3 canales de colores: azul verde y rojo (blue green red)
    azul=imagen_original[:,:,0]
    verde=imagen_original[:,:,1]
    rojo=imagen_original[:,:,2]
    #Aplicamos la formula NTSC para convertir a escala de grises en 8 bits
    imagen_gris=0.114*azul+0.587*verde+0.299*rojo
    #Se convierte a enteros de 8 bits
    imagen_gris=np.array(imagen_gris).astype(np.uint8)
    return imagen_gris
