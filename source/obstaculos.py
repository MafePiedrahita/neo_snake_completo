import pygame
import random

class Obstaculo:
    def __init__(self, ancho_tablero, alto_tablero, tam_celda):
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.tam_celda = tam_celda
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.imagen = pygame.image.load("assets/imagenes/obstaculo.png")
        self.imagen = pygame.transform.scale(self.imagen, (tam_celda, tam_celda))

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x * self.tam_celda, self.y * self.tam_celda))


