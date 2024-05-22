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
