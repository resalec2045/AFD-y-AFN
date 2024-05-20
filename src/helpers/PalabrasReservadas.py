class PalabrasReservadas:
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

    @classmethod
    def get_palabras_reservadas(cls):
        return cls.palabras_reservadas
