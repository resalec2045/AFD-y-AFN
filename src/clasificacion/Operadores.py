from src.generarAFD import GenerarAFD
from src.helpers.PalabrasReservadas import PalabrasReservadas


def determinarOperadores(elementos, indice):
    elemento1 = elementos[0]
    elemento2 = elementos[2]
    operacionCreada = elementos[1]
    operacionTipo = PalabrasReservadas.get_palabras_reservadas().get(elementos[1], 'Error')

    if operacionTipo == 'Aritméticos':
        imprimirAritmeticos(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Comparación':
        imprimirComparacion(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Lógicos':
        imprimirLogicos(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Asignación':
        imprimirAsignacion(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Incremento':
        imprimirIncremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Decremento':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Apertura_Y_Cierre':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Terminal':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Separador':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Valor_de_asignacion':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Identificadores':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Palabras_reservadas':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    elif operacionTipo == 'Tipo_de_dato':
        imprimirDecremento(indice, operacionTipo, operacionCreada)
    else:
        return None


def imprimirAritmeticos(indice, tipoOperacion, operacion):
    GenerarAFD.mostrar_automata(operacion, tipoOperacion)
    print(f"{indice:<15} {tipoOperacion:<20} {operacion:<15}")


def imprimirComparacion(indice, tipoOperacion, operacion):
    GenerarAFD.mostrar_automata(operacion, tipoOperacion)
    print(f"{indice:<15} {tipoOperacion:<20} {operacion:<15}")


def imprimirLogicos(indice, tipoOperacion, operacion):
    GenerarAFD.mostrar_automata(operacion, tipoOperacion)
    print(f"{indice:<15} {tipoOperacion:<20} {operacion:<15}")


def imprimirAsignacion(indice, tipoOperacion, operacion):
    GenerarAFD.mostrar_automata(operacion, tipoOperacion)
    print(f"{indice:<15} {tipoOperacion:<20} {operacion:<15}")


def imprimirIncremento(indice, tipoOperacion, operacion):
    GenerarAFD.mostrar_automata(operacion, tipoOperacion)
    print(f"{indice:<15} {tipoOperacion:<20} {operacion:<15}")


def imprimirDecremento(indice, tipoOperacion, operacion):
    GenerarAFD.mostrar_automata(operacion, tipoOperacion)
    print(f"{indice:<15} {tipoOperacion:<20} {operacion:<15}")
