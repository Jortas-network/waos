
---

### ✅ `README.md`

```markdown
# 📸 Filtros de Imágenes en Python

Este proyecto permite aplicar distintos filtros a una imagen, como:
- Filtro de media (promedio)
- Filtro de mediana
- Filtro Laplaciano
- Filtro de Sobel

Permite cargar una imagen a color o en escala de grises, aplicar el filtro deseado, y mostrar el resultado.

---

## 🗂️ Estructura del proyecto

```

image-filters/
│
├── main.py
├── filters/
│   ├── **init**.py
│   ├── media.py
│   ├── mediana.py
│   ├── laplaciano.py
│   └── sobel.py
└── README.md

````

---

## 🚀 Requisitos

Instala las dependencias necesarias con:

```bash
pip install opencv-python numpy matplotlib
````

---

## 🧪 Cómo ejecutar

1. Coloca la imagen que deseas usar en la misma carpeta que `main.py` (o ajusta la ruta).
2. Ejecuta el archivo principal:

```bash
python main.py
```

3. Se te preguntará qué filtro deseas aplicar:

   ```
   Elige un filtro:
   1 - Media
   2 - Mediana
   3 - Laplaciano
   4 - Sobel
   ```

4. Se mostrará la imagen original y la filtrada usando `matplotlib`.

---

## 📌 Notas

* Los filtros Laplaciano y Sobel siempre trabajan en escala de grises.
* Si la imagen de entrada es a color, se convierte automáticamente.
* El código está modularizado para facilitar pruebas y mantenimiento.

---

## 🧑‍💻 Autor

Desarrollado por Jorgito tu terror
```
Carreenme en las EU pofa

Mas preguntas al 987654321 sapaso

---


