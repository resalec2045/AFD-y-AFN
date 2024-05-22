import textwrap
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from clasificacion import Operadores
from src.helpers.PalabrasReservadas import PalabrasReservadas
import os


class Aplicacion:
    def __init__(self, root, nombre_archivo, palabras_reservadas):
        self.root = root
        self.root.title("Generador de Autómatas")

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
        root.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        frame = ttk.Frame(notebook)
        notebook.add(frame, text="interfaz")

        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="n", width=ventana_ancho - 20)

        lineas = []

        if os.path.isfile(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
        else:
            print(f"Error: El archivo '{nombre_archivo}' no se encuentra en el directorio actual.")
            return

        # Encabezados de la tabla
        self.titulo = ttk.Label(content_frame, text="Tabla de Operadores")
        self.titulo.pack()
        self.texto = tk.Label(content_frame, text=f"{'Posicion':<15} {'Categoria':<20} {'Palabra reservada':<15}")
        self.texto.pack()

        for indice, linea in enumerate(lineas, start=1):
            elementos = linea.strip().split()
            if len(elementos) == 3:
                Operadores.determinarOperadores(elementos, indice)
                operacionTipo = PalabrasReservadas.get_palabras_reservadas().get(elementos[1], 'Error')
                self.texto = tk.Label(content_frame, text=f"{indice:<15} {operacionTipo:<20} {elementos[1]:<15}")
                self.texto.pack()

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

        # Obtiene la ruta del directorio donde se encuentra el archivo actual
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        # Construye la ruta base relativa al directorio actual
        directorio_base = os.path.join(directorio_actual, "automatas")
        subdirectorios = ["Aritméticos", "Comparación", "Asignación", "Lógicos", "Incremento", "Decremento",
                          "Apertura_Y_Cierre", "Terminal", "Separador", "Palabras_reservadas", "Identificadores", "Valor_de_asignacion", "Tipo_de_dato"]

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
        canvas.create_window((0, 0), window=image_frame, anchor="n")

        for archivo in os.listdir(ruta):
            if archivo.endswith(".png"):
                img_path = os.path.join(ruta, archivo)
                image = Image.open(img_path)
                photo = ImageTk.PhotoImage(image)

                label = tk.Label(image_frame, image=photo)
                label.image = photo  # Keep a reference!
                label.pack()


if __name__ == "__main__":
    nombre_archivo = 'operaciones.txt'
    root = tk.Tk()
    app = Aplicacion(root, nombre_archivo, PalabrasReservadas.get_palabras_reservadas())
    root.mainloop()
