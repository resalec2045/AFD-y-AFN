from clasificacion import Operadores
from src.helpers.PalabrasReservadas import PalabrasReservadas
import os

def leer_y_procesar_archivo(nombre_archivo, palabras_reservadas):
    lineas = []

    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
    else:
        print(f"Error: El archivo '{nombre_archivo}' no se encuentra en el directorio actual.")
        return

    # Encabezados de la tabla
    print(f"{'Posicion':<15} {'Categoria':<20} {'Palabra reservada':<15}")
    print('-' * 50)

    for indice, linea in enumerate(lineas, start=1):
        elementos = linea.strip().split()
        if len(elementos) == 3:
            # Importar la clase Operadores
            Operadores.determinarOperadores(elementos, indice)

nombre_archivo = 'operaciones.txt'
leer_y_procesar_archivo(nombre_archivo, PalabrasReservadas.get_palabras_reservadas())