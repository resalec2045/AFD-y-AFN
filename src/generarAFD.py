import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from automathon import DFA
import os


class GenerarAFD:
    @staticmethod
    def crear_automata(palabra):
        estados = {'q' + str(i) for i in range(len(palabra) + 1)}
        sigma = set(palabra)
        delta = {}
        for i, letra in enumerate(palabra):
            estado = 'q' + str(i)
            siguiente_estado = 'q' + str(i + 1)
            if estado not in delta:
                delta[estado] = {}
            delta[estado][letra] = siguiente_estado
        estado_inicial = 'q0'
        estado_final = {'q' + str(len(palabra))}
        return estados, sigma, delta, estado_inicial, estado_final

    @staticmethod
    def mostrar_automata(palabra, ruta_archivo):
        estados, sigma, delta, estado_inicial, estado_final = GenerarAFD.crear_automata(palabra)
        automata = DFA(estados, sigma, delta, estado_inicial, estado_final)
        os.makedirs(f"automatas/{ruta_archivo}", exist_ok=True)

        automata.view(
            file_name=f"automatas/{ruta_archivo}/coso{palabra}",
            node_attr={'fontsize': '20'},
            edge_attr={'fontsize': '20pt'}
        )

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Autómatas")

        self.btn_generar = tk.Button(root, text="Generar Autómatas", command=self.generar_automatas)
        self.btn_generar.pack(pady=20)

    def generar_automatas(self):
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title("Autómatas Generados")

        notebook = ttk.Notebook(nueva_ventana)
        notebook.pack(fill='both', expand=True)

        directorio_base = "/Users/crisbal/Desktop/proyecto-tlf/AFD-y-AFN/src/automatas/"
        subdirectorios = ["Aritméticos", "Comparación", "Asignación"]

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
