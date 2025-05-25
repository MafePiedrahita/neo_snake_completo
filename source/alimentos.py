import random

TAM_CELDA = 50

class Alimentos:
    def __init__(self, tipo: str, ancho_tablero: int, alto_tablero: int):
        self.tipo = tipo
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.x = 0
        self.y = 0
        self.imagen = None
        self.nueva_posicion()

    def nueva_posicion(self):
        self.x = random.randint(0, self.ancho_tablero - 1)
        self.y = random.randint(0, self.alto_tablero - 1)

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

class Pera(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int, recursos):
        super().__init__("Pera", ancho_tablero, alto_tablero)
        self.imagen = recursos.get_imagen("pera")

class Ciruela(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int, recursos):
        super().__init__("Ciruela", ancho_tablero, alto_tablero)
        self.imagen = recursos.get_imagen("ciruela")