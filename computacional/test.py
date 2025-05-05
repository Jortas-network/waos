import cv2
import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen en escala de grises con ruido
imagen = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

# Filtro de mediana
mediana = cv2.medianBlur(imagen, 3)

# Filtro de media (promedio)
media = cv2.blur(imagen, (3, 3))

# Mostrar resultados
plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.title("Original con ruido")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Filtro Mediana")
plt.imshow(mediana, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Filtro Media")
plt.imshow(media, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
