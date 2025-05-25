import pygame
import random

TAM_CELDA = 50
AZUL = (0, 0, 225)

class PowerupCongelar:
    def __init__(self, ancho_tablero, alto_tablero):
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.visible = True
        self.color = AZUL

    def dibujar(self, superficie):
        if self.visible:
            rect = pygame.Rect(self.x * TAM_CELDA, self.y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
            pygame.draw.rect(superficie, self.color, rect)

    def activar(self):
        self.visible = False
