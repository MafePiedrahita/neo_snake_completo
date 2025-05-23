import pygame
import random

blanco= (255, 255, 255)

class Obstaculo:
    def __init__(self, ancho_tablero, alto_tablero, tam_celda):
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.tam_celda = tam_celda
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.color = blanco
    def dibujar(self, superficie):
        rect = pygame.Rect(
            self.x * self.tam_celda, self.y * self.tam_celda,
            self.tam_celda, self.tam_celda
        )
        pygame.draw.rect(superficie, self.color, rect)


