import pygame
import random

azul = (0, 0, 225)
TAM_CELDA = 30

class PowerupCongelar:
    def __init__(self, ancho_tablero, alto_tablero):
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.color = azul
        self.visible = True
    def dibujar(self, superficie):
        if self.visible:
            rect = pygame.Rect(self.x * TAM_CELDA, self.y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
            pygame.draw.rect(superficie, self.color, rect)

    def activar(self):
        self.visible = False
