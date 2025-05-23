import pygame
import random
TAM_CELDA = 30

verde = (0,128,0)
morado = (128,0,128)

class Alimentos:
    def __init__(self, tipo: str, ancho_tablero: int, alto_tablero: int, color ):
        self.tipo = tipo
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.color = color
        self.nueva_posicion()

    def nueva_posicion(self):
        self.x = random.randint(0, self.ancho_tablero - 1)
        self.y = random.randint(0, self.alto_tablero - 1)

    def dibujar(self, superficie):
        rect = pygame.Rect(self.x * TAM_CELDA, self.y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
        pygame.draw.rect(superficie, self.color, rect)

class Pera(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int):
        super().__init__("Pera", ancho_tablero, alto_tablero, morado)


