class MyApp():

    # def __init__(self):
    #     self.qNombre = list()
    #     self.qIzquierda = list()
    #     self.estadosQ = list()
    #     self.textos = [
    #         ["q0,q1", "q0,q1"],
    #         ["q2", "q0,q2"],
    #         ["none", "none"]
    #     ]
    #     self.campoQ0 = "q0"
    #     self.campoF = "q2"
    #     self.filas = 3
    #
    #     self.calcularCadena()

    def __init__(self):
        self.qNombre = list()
        self.qIzquierda = list()
        self.estadosQ = list()
        self.textos = []
        self.campoQ0 = ""
        self.campoF = ""
        self.filas = 0
        self.solicitar_informacion()

    def solicitar_informacion(self):

        self.filas = int(input("Ingrese la cantidad de filas: "))

        self.textos = []
        for i in range(self.filas):
            entrada = input(f"Ingrese los textos para la fila {i}: ").split(" ")
            self.textos.append(entrada)

        self.campoQ0 = input("Ingrese el valor del estado inicial: ")

        self.campoF = input("Ingrese el valor para el estado final: ")

        self.calcularCadena()

    def calcularCadena(self):

        for i in range(0, self.filas):
            self.estadosQ.append([
                self.retornarNumeroStr(self.textos[i][0]),
                self.retornarNumeroStr(self.textos[i][1])
            ])

        self.tablaConversion()
        self.cargarR()

    def tablaConversion(self):
        self.arreglo_tabla_0_1 = list()
        self.qIzquierda = list()

        self.qActualNumerica = self.retornarNumeroStr(self.campoQ0)  # q1,q2 -> 1  2
        self.qIzquierda.append(self.retornarEstructuraOriginalQn(self.qActualNumerica))  # 1  2 -> q1,q2

        fila_iteracion = 0

        while fila_iteracion < len(self.qIzquierda):
            self.arreglo_tabla_0_1.append([0] * 2)  # Agregar nuevo espacio a la lista de conversion

            if self.qIzquierda[fila_iteracion] != 'none':  # Si el valor actual de la izquierda NO es none...

                if len(self.retornarNumeroStr(self.qIzquierda[fila_iteracion])) > 1:  # Si hay mas de dos Q's

                    for k in range(0, 2):  # Se toman los estados para evaluar 0 y 1 independientemente
                        conjuntos = list()
                        for j in list(self.retornarNumeroStr(
                                self.qIzquierda[fila_iteracion])):  # Para cada estado... (12 -> 1)

                            conjunto_actual = self.estadosQ[int(j)][
                                k]  # Se toma el conjunto actual. Ex: 1 -> 0: 1,2; 1: 2

                            if conjunto_actual != 'none':  # Si es diferente a la nada...
                                conjuntos.append(conjunto_actual)
                                qActualNumerica = "".join(
                                    set(''.join(conjuntos)))  # Se eliminan los duplicados con conversiones

                                # Se agrega a la tabla conversion....
                                self.arreglo_tabla_0_1[fila_iteracion][k] = self.retornarEstructuraOriginalQn(
                                    qActualNumerica)

                        # Si el valor obtenido no esta en la izquierda se agrega
                        if self.arreglo_tabla_0_1[fila_iteracion][k] not in self.qIzquierda:
                            self.qIzquierda.append(self.arreglo_tabla_0_1[fila_iteracion][k])

                else:  # Si solo es un estado. Ex: q1
                    for j in range(0, 2):
                        qActualNumerica = self.estadosQ[int(self.retornarNumeroStr(self.qIzquierda[fila_iteracion]))][j]

                        if qActualNumerica != 'none':  # Si el valor obtenido NO es nada...
                            qActual_original = self.retornarEstructuraOriginalQn(qActualNumerica)
                            self.arreglo_tabla_0_1[fila_iteracion][j] = qActual_original

                            if self.arreglo_tabla_0_1[fila_iteracion][
                                j] not in self.qIzquierda:  # Si lo obtenido no esta en izq...
                                self.qIzquierda.append(self.arreglo_tabla_0_1[fila_iteracion][j])

                        else:  # Si el valor SI es nada, al ser un unico estado, se evalua

                            if 'none' not in self.qIzquierda:
                                self.qIzquierda.append('none')
                            self.arreglo_tabla_0_1[fila_iteracion][j] = 'none'

            else:  # Si el valor izq actual es NONE, entonces en su tabla de estados se asiga a NONE
                self.arreglo_tabla_0_1[fila_iteracion][0] = 'none'
                self.arreglo_tabla_0_1[fila_iteracion][1] = 'none'

            fila_iteracion = fila_iteracion + 1

        self.cargarSegundaTabla()

    def cargarSegundaTabla(self):

        print("\n Tabla intermedia \n")

        resultado = ""
        for iteracion_tabla in range(len(self.qIzquierda)):
            resultado += "Fila {}: 0 -> {}, 1 -> {}\n".format(
                iteracion_tabla,
                self.arreglo_tabla_0_1[iteracion_tabla][0],
                self.arreglo_tabla_0_1[iteracion_tabla][1]
            )
        print(resultado)

    def cargarR(self):

        print("\n Tabla final \n")

        resultado = ""
        for iteracion in range(len(self.qIzquierda)):
            resultado += "X{}: 0 -> X{}, 1 -> X{}\n".format(
                iteracion,
                self.qIzquierda.index(self.arreglo_tabla_0_1[iteracion][0]),
                self.qIzquierda.index(self.arreglo_tabla_0_1[iteracion][1])
            )
        print(resultado)

    def retornarEstructuraOriginalQn(self, valor):
        valor = list(valor)
        valor.sort()
        estructura_original = ''

        for j in list(valor):
            estructura_original = estructura_original + 'q{},'.format(j)

        return estructura_original[:len(estructura_original) - 1]

    def retornarNumeroStr(self, texto):
        return texto.lower().translate({ord(j): None for j in ' q,'})


if __name__ == "__main__":
    MyApp()
