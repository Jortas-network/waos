import cv2

def cargar_imagen(ruta):
    imagen = cv2.imread(ruta)
    if imagen is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta}")
    return imagen

def cargar_imagen_gris(ruta):
    imagen = cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta}")
    return imagen

def resize_image(imagen, width=None, height=None):
    if width is not None:
        r = width / imagen.shape[1]
        dim = (width, int(imagen.shape[0] * r))
    elif height is not None:
        r = height / imagen.shape[0]
        dim = (int(imagen.shape[1] * r), height)
    else:
        return imagen
    return cv2.resize(imagen, dim)

def mostrar_imagen(imagen,texto):
    cv2.imshow(texto, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None