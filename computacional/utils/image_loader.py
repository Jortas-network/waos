import cv2

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {path}")
    return image

def resize_image(image, width=None, height=None):
    if width is not None:
        r = width / image.shape[1]
        dim = (width, int(image.shape[0] * r))
    elif height is not None:
        r = height / image.shape[0]
        dim = (int(image.shape[1] * r), height)
    else:
        return image
    return cv2.resize(image, dim)
