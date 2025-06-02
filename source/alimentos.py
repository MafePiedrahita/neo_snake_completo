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
        self.nueva_posicion()  # Inicializa con posición aleatoria

    def nueva_posicion(self, posiciones_prohibidas=None):
        if posiciones_prohibidas is None:
            posiciones_prohibidas = set()

        while True:
            self.x = random.randint(0, self.ancho_tablero - 1)
            self.y = random.randint(0, self.alto_tablero - 1)
            if (self.x, self.y) not in posiciones_prohibidas:
                break

    def obtener_posicion(self):
        return (self.x, self.y)

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

    def mover_hacia(self, objetivo):
        objetivo_x, objetivo_y = objetivo

        if self.x < objetivo_x:
            self.x += 1
        elif self.x > objetivo_x:
            self.x -= 1

        if self.y < objetivo_y:
            self.y += 1
        elif self.y > objetivo_y:
            self.y -= 1

class Pera(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int, recursos):
        super().__init__("Pera", ancho_tablero, alto_tablero)
        self.imagen = recursos.get_imagen("pera")

class Ciruela(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int, recursos):
        super().__init__("Ciruela", ancho_tablero, alto_tablero)
        self.imagen = recursos.get_imagen("ciruela")
