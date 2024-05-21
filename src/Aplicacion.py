import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Autómatas")

        self.btn_generar = tk.Button(root, text="Generar Autómatas", command=self.generar_automatas)
        self.btn_generar.pack(pady=20)

    def generar_automatas(self):
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title("Autómatas Generados")

        # Obtener las dimensiones de la pantalla
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()

        # Definir el tamaño de la nueva ventana
        ventana_ancho = int(pantalla_ancho * 0.8)
        ventana_alto = int(pantalla_alto * 0.8)

        # Calcular las coordenadas para centrar la ventana
        pos_x = (pantalla_ancho // 2) - (ventana_ancho // 2)
        pos_y = (pantalla_alto // 2) - (ventana_alto // 2)

        # Configurar las dimensiones y posición de la nueva ventana
        nueva_ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")

        notebook = ttk.Notebook(nueva_ventana)
        notebook.pack(fill='both', expand=True)

        directorio_base = "D://universidad/AFD-y-AFN/src/automatas/"
        subdirectorios = ["Aritméticos", "Comparación", "Asignacion", "Lógicos", "Incremento", "Decremento"]

        for subdir in subdirectorios:
            ruta_completa = os.path.join(directorio_base, subdir)
            self.crear_pestana(notebook, subdir, ruta_completa)

    def crear_pestana(self, notebook, titulo, ruta):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=titulo)

        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        image_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=image_frame, anchor="nw")

        for archivo in os.listdir(ruta):
            if archivo.endswith(".png"):
                img_path = os.path.join(ruta, archivo)
                image = Image.open(img_path)
                photo = ImageTk.PhotoImage(image)

                label = tk.Label(image_frame, image=photo)
                label.image = photo  # Keep a reference!
                label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
