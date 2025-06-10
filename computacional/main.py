import cv2
from filtros import media, mediana, laplaciano, sobel, media16, laplaciano8
from utils.image_loader import cargar_imagen, resize_image, cargar_imagen_gris, mostrar_imagen

def main():
    ruta_imagen = input("Ruta de la imagen: ")
    imagen = cargar_imagen(ruta_imagen)
    imagen_escalagris = cargar_imagen_gris(ruta_imagen)
    bucle = True
    print("Elige un filtro:")
    print("1. Media(1/9)\n2. Media(1/16)\n3. Mediana\n4. Laplaciano(-1,4)\n5. Laplaciano (-1,8)\n6. Sobel")
    print("Extra:")
    print("A. Ver imagen original\nB. Ver imagen en escala de grises\nX. Salir")
    texto = "ASD"
    while(bucle):
        eleccion = input("Opción: ")
        if eleccion == "1":
            resultado = media.aplicar(imagen_escalagris)
            texto = "Filtro de Media (1/9)"
        elif eleccion == "2":
            resultado = media16.aplicar(imagen_escalagris)
            texto = "Filtro de Media (1/16)"
        elif eleccion == "3":
            resultado = mediana.aplicar(imagen_escalagris)
            texto = "Filtro de Mediana"
        elif eleccion == "4":
            resultado = laplaciano.aplicar(imagen_escalagris)
            texto = "Filtro Laplaciano (-1,4)"
        elif eleccion == "5":
            resultado = laplaciano8.aplicar(imagen_escalagris)
            texto = "Filtro Laplaciano (-1,8)"
        elif eleccion == "6":
            resultado = sobel.aplicar(imagen_escalagris)
            texto = "Filtro de Sobel"
        elif eleccion == "A":
            resultado = imagen
            texto = "Imagen original"
        elif eleccion == "B":
            resultado = imagen_escalagris
            texto = "Imagen en escala de grises"
        elif eleccion == "X":
            bucle = False
        else:
            print("Opción inválida.")
            continue
        if bucle:
            resultado = resize_image(resultado,512,512)
            mostrar_imagen(resultado,texto)

if __name__ == "__main__":
    main()
