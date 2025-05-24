import pygame
import random
TAM_CELDA = 50

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
        pass

class Pera(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int):
        super().__init__("Pera", ancho_tablero, alto_tablero)
        self.imagen = pygame.image.load("assets/imagenes/pera.png")
        self.imagen = pygame.transform.scale(self.imagen, (TAM_CELDA, TAM_CELDA))

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

class Ciruela(Alimentos):
    def __init__(self, ancho_tablero: int, alto_tablero: int):
        super().__init__("Ciruela", ancho_tablero, alto_tablero)
        self.imagen = pygame.image.load("assets/imagenes/ciruela.png")
        self.imagen = pygame.transform.scale(self.imagen, (TAM_CELDA, TAM_CELDA))

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))