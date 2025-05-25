import random

TAM_CELDA = 50

class Obstaculo:
    def __init__(self, ancho_tablero, alto_tablero, recursos):
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.imagen = recursos.get_imagen("obstaculo")

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x * self.tam_celda, self.y * self.tam_celda))