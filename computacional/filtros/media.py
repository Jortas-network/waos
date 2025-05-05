import cv2

def apply(image, ksize=3):
    return cv2.medianBlur(image, ksize)
