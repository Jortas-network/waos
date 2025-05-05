import cv2
from filtros import media, mediana, laplaciano, sobel
from utils.image_loader import load_image, resize_image

def main():
    image_path = input("Ruta de la imagen: ")
    image = load_image(image_path)
    image = resize_image(image, width=512)  # O cualquier tamaño estándar

    print("Elige un filtro:")
    print("1. Media\n2. Mediana\n3. Laplaciano\n4. Sobel")
    choice = input("Opción: ")

    if choice == "1":
        result = media.apply(image)
    elif choice == "2":
        result = mediana.apply(image)
    elif choice == "3":
        result = laplaciano.apply(image)
    elif choice == "4":
        result = sobel.apply(image)
    else:
        print("Opción inválida.")
        return

    cv2.imshow("Resultado", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
