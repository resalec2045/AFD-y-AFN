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
            elemento1 = elementos[0]
            elemento2 = elementos[2]
            operacionCreada = elementos[1]  # Palabra reservadas
            operacionTipo = palabras_reservadas.get(elementos[1], 'Error')
            # Impresión de la fila de la tabla
            print(f"{indice:<15} {operacionTipo:<20} {operacionCreada:<15}")

# Ejemplo de uso
nombre_archivo = 'operaciones.txt'
# Diccionario de palabras reservadas
palabras_reservadas = {
    'sumis': 'Aritméticos',
    'sumisnt': 'Aritméticos',
    'idk': 'Aritméticos',
    'dc': 'Aritméticos',
    '~~': 'Comparación',
    '~nt': 'Comparación',
    '+-': 'Comparación',
    '-+': 'Comparación',
    '+~': 'Comparación',
    '~+': 'Comparación',
    'enefecto': 'Lógicos',
    'otracosa': 'Lógicos',
    'nonas': 'Lógicos',
    '~': 'Asignación',
    'sumisx2': 'Incremento',
    'sumisx2nt': 'Decremento'
}

leer_y_procesar_archivo(nombre_archivo, palabras_reservadas)
