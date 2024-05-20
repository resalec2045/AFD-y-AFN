from automathon import DFA


class GenerarAFD:

    @staticmethod
    def crear_automata(palabra):

        # print(f"Creando autómata para la palabra '{palabra}'")

        # Definir los estados
        estados = {'q' + str(i) for i in range(len(palabra) + 1)}

        # Definir el alfabeto sigma como el conjunto de caracteres de la palabra
        sigma = set(palabra)

        # Definir la función de transición delta
        delta = {}
        for i, letra in enumerate(palabra):
            estado = 'q' + str(i)
            siguiente_estado = 'q' + str(i + 1)
            if estado not in delta:
                delta[estado] = {}
            delta[estado][letra] = siguiente_estado

        # Asegurarse de que cada estado tenga una transición para cada símbolo en sigma
        for estado in estados:
            if estado not in delta:
                delta[estado] = {}
            for simbolo in sigma:
                if simbolo not in delta[estado]:
                    delta[estado][simbolo] = estado  # Transición a sí mismo si no está definido

        # Definir el estado inicial
        estado_inicial = 'q0'

        # Definir el estado final
        estado_final = {'q' + str(len(palabra))}

        return estados, sigma, delta, estado_inicial, estado_final

    @staticmethod
    def mostrar_automata(palabra):
        # Crear los componentes del autómata a partir de la palabra
        estados, sigma, delta, estado_inicial, estado_final = GenerarAFD.crear_automata(palabra)

        # Mostrar los detalles del autómata
        # print(f"Estados: {estados}")
        # print(f"Alfabeto: {sigma}")
        # print(f"Función de transición: {delta}")
        # print(f"Estado inicial: {estado_inicial}")
        # print(f"Estados finales: {estado_final}")

        # Crear el autómata DFA
        automata = DFA(estados, sigma, delta, estado_inicial, estado_final)

        # Graficar el autómata (si la librería automathon permite esta funcionalidad)
        automata.view(
            file_name="automatas/" + palabra,
            node_attr={'fontsize': '20'},
            edge_attr={'fontsize': '20pt'}
        )

