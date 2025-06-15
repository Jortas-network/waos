import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from matplotlib import pyplot as plt
from filtros import media, mediana, laplaciano, sobel, media16, laplaciano8
from utils.image_loader import cargar_imagen, cargar_imagen_gris
class FiltroGUI(tk.Tk):
    def __init__(self,root):
        #Constructor
        self.root=root
        self.root.title("Filtrado de Imagenes - Grupo 3")
        self.root.geometry("500x720")
        self.root.configure(bg="#2e2e2e")
        self.imagen_original = None
        self.imagen_actual = None
        self.imagen_escalagris = None
        self.ruta_imagen = None
        self.ruta_imagen_txt = tk.StringVar()
        self.ruta_imagen_txt.set("No se seleccionó una imagen")
        self.filtros_mostrados = False
        self.botones_filtros = []
        self.menu_inicial()
    def limpiar_interfaz(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    def menu_inicial(self):
        self.limpiar_interfaz()
        self.ruta_imagen_txt.set("No se seleccionó una imagen")

        tk.Label(self.root, text="Filtrado de Imágenes", font=("Helvetica", 20, "bold"),
                 bg="#2e2e2e", fg="white").pack(pady=10)

        logo = """
              *                    
             ***                    
       **   ****        *           
     **     *****        **         
     **     *******      ***        
    ***     ********     ***        
    ***      *******     ***        
    ****       *****    ****        
    *****       ****   *****        
     *******    *** ********        
      *********************         
       ******************           
         **************             
              ****                  
        """
        tk.Label(self.root, text=logo, font=("Courier", 8), bg="#2e2e2e", fg="red").pack()

        tk.Label(self.root, textvariable=self.ruta_imagen_txt, font=("Arial", 9),
                 bg="#2e2e2e", fg="white", wraplength=450).pack(pady=5)

        botones = [
            ("Tomar foto", self.tomar_foto),
            ("Cargar imagen", self.cargar_imagen),
            ("Instrucciones", self.instrucciones),
            ("Créditos", self.creditos)
        ]
        for texto, comando in botones:
            tk.Button(self.root, text=texto, command=comando, width=40, bg="#444444", fg="white").pack(pady=3)
    def menu_post_imagen(self):
        self.limpiar_interfaz()
        self.filtros_mostrados = False
        self.botones_filtros = []

        tk.Label(self.root, text="Imagen cargada", font=("Helvetica", 16, "bold"),
                 bg="#2e2e2e", fg="white").pack(pady=10)

        opciones = [
            ("Ver imagen", self.mostrar_imagen),
            ("Agregar ruido", self.agregar_ruido),
            ("Quitar ruido", self.quitar_ruido),
            ("Ver en escala de grises", self.mostrar_imagen_escalagris),
            ("Filtros", self.toggle_filtros)
        ]

        for texto, comando in opciones:
            tk.Button(self.root, text=texto, command=comando, width=40, bg="#444444", fg="white").pack(pady=3)

        # Botón volver al final
        self.boton_volver = tk.Button(self.root, text="Volver al menú", command=self.menu_inicial,
        width=40, bg="#ff4444", fg="white")
        self.boton_volver.pack(pady=10)
    def toggle_filtros(self):
        if self.filtros_mostrados:
            for boton in self.botones_filtros:
                boton.destroy()
            self.botones_filtros.clear()
            self.filtros_mostrados = False
        else:
            filtros = [
                ("Filtro Media 1/9", lambda: self.aplicar_filtro(media.aplicar, "Media 1/9")),
                ("Filtro Media 1/16", lambda: self.aplicar_filtro(media16.aplicar, "Media 1/16")),
                ("Filtro Mediana", lambda: self.aplicar_filtro(mediana.aplicar, "Mediana")),
                ("Filtro Laplace 4", lambda: self.aplicar_filtro(laplaciano.aplicar, "Laplace 4")),
                ("Filtro Laplace 8", lambda: self.aplicar_filtro(laplaciano8.aplicar, "Laplace 8")),
                ("Filtro Sobel", lambda: self.aplicar_filtro(sobel.aplicar, "Sobel")),
            ]

            for texto, comando in filtros:
                btn = tk.Button(self.root, text=texto, command=comando, width=40, bg="#555555", fg="white")
                btn.pack(pady=2, before=self.boton_volver)  # Se insertan antes del botón 'Volver'
                self.botones_filtros.append(btn)

            self.filtros_mostrados = True
    def tomar_foto(self):
        cap = cv2.VideoCapture(0)
        messagebox.showinfo("Instrucciones", "Presiona 'ESPACIO' para tomar la foto y 'ESC' para cancelar.")
        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showinfo("Error", "No se ha detectado una camara")
                break
            cv2.imshow('Presiona ESPACIO para capturar', frame)
            key = cv2.waitKey(1)
            if key == 27:
                cap.release()
                cv2.destroyAllWindows()
                return
            elif key == 32:
                self.imagen_original = frame.copy()
                self.imagen_actual = self.imagen_original.copy()
                self.imagen_escalagris = cv2.cvtColor(self.imagen_actual, cv2.COLOR_BGR2GRAY)
                cap.release()
                cv2.destroyAllWindows()
                self.ruta_imagen_txt.set("Foto tomada con cámara")
                self.menu_post_imagen()
                break
    def agregar_ruido(self):
        if self.imagen_actual is None:
            messagebox.showerror("Error", "No hay imagen cargada")
            return
        ruido = self.imagen_actual.copy()
        filas, columnas, _ = ruido.shape
        num_ruido = int(0.01 * filas * columnas)
        for _ in range(num_ruido):
            x, y = np.random.randint(0, filas), np.random.randint(0, columnas)
            ruido[x, y] = [255, 255, 255] if np.random.rand() < 0.5 else [0, 0, 0]
        self.imagen_actual = ruido
        self.imagen_escalagris = cargar_imagen_gris(self.imagen_actual)
        messagebox.showinfo("Listo", "Se agregó ruido a la imagen")
    def quitar_ruido(self):
        if self.imagen_original is not None:
            self.imagen_actual = self.imagen_original.copy()
            self.imagen_escalagris = cargar_imagen_gris(self.imagen_actual)
            messagebox.showinfo("Restaurado", "Se restauró la imagen original")
    def cargar_imagen(self):
        ruta_aux = filedialog.askopenfilename(title="Seleccionar imagen",
        filetypes=[("Archivos de imagen","*.png *.jpg *.jpeg *.bmp *.tif")])
        if ruta_aux:
            self.ruta_imagen=str(ruta_aux)
            self.ruta_imagen_txt.set(f"Ruta: {ruta_aux}")
            self.imagen_original=cargar_imagen(self.ruta_imagen)
            self.imagen_actual=self.imagen_original.copy()
            self.imagen_escalagris=cargar_imagen_gris(self.imagen_original)
            self.menu_post_imagen()
        else:
            self.ruta_imagen_txt.set("No se seleccionó una imagen")
    def instrucciones(self):
        texto = (
            "1. Carga una imagen desde tu galería o toma una foto.\n"
            "2. Visualiza la imagen original o en escala de grises.\n"
            "3. Agrega o quita ruido.\n"
            "4. Aplica el filtro que desees.\n"
            "5. Puedes volver al menú para reiniciar el proceso.\n"
        )
        messagebox.showinfo("Instrucciones", texto)
    def creditos(self):
        texto = (
            "Filtrado de Imágenes - Grupo 3\n"
            "Dyron Huapaya Galindo\n"
            "Giulian Sebastián Meneses Sulca\n"
            "José Diego Bautista Rivera\n"
            "Jorge Francisco Taipe Sangama\n"
            "Gianmarco Alexander Castañeda Sinarahua\n"
            "UPC - 2025"
        )
        messagebox.showinfo("Créditos", texto)
    def mostrar_imagen(self):
        #Mostrando la imagen original si se selecciono
        if self.imagen_actual is not None:
            imagen_rgb=cv2.cvtColor(self.imagen_actual,cv2.COLOR_BGR2RGB)
            plt.imshow(imagen_rgb)
            plt.title("Imagen actual")
            plt.axis("off")
            plt.show()
        else:
            messagebox.showerror("Error", "No hay imagen")
    def mostrar_imagen_escalagris(self):
        #Mostrando la imagen en escala de grises 8 bits
        if self.imagen_escalagris is not None:
            #Se agrega cmap="gray" para que los valores 255 en escala de grises se vean blanco y los valores 0 se vean negro
            plt.imshow(self.imagen_escalagris, cmap="gray")
            plt.title("Escala de grises")
            plt.axis("off")
            plt.show()
        else:
            messagebox.showerror("Error", "No hay imagen")
    def aplicar_filtro(self, funcion, nombre):
        if self.imagen_escalagris is not None:
            resultado = funcion(self.imagen_escalagris)
            plt.imshow(resultado, cmap="gray")
            plt.title(f"Filtro {nombre}")
            plt.axis("off")
            plt.show()
        else:
            messagebox.showerror("Error", "No hay imagen")

if __name__ == "__main__":
    root=tk.Tk()
    app=FiltroGUI(root)
    root.mainloop()
