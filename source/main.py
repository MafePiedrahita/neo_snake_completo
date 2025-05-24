import pygame
import sys

from pygame.examples.go_over_there import clock

from alimentos import Pera, Ciruela
from obstaculos import Obstaculo
from powerups import PowerupCongelar
from musica import cargar_musica
from puntajes import mostrar_puntajes
from jugadores import Jugador
from logica_juego import manejar_eventos, actualizar_estado
from source.alimentos import TAM_CELDA

pygame.init()
cargar_musica("assets/sonidos/musica_fondo.mp3")

TAM_CELDA = 30
ANCHO, ALTO = 600, 600
FPS = 10
ANCHO_CELDAS = ANCHO // TAM_CELDA
ALTO_CELDAS = ALTO // TAM_CELDA

NEGRO = (0, 0, 0)
BLANCO = (225, 225, 0)
AMARILLO = (255, 255, 0)
verde = (0, 128, 0)
ROJO = (255, 0, 0)

clock = pygame.time.Clock()

jugador1 = Jugador({
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT
}, verde)

jugador2 = Jugador({
    "UP": pygame.K_w,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d
}, ROJO)

jugadores = {
    "jugador1": jugador1,
    "jugador2": jugador2
}

pera = Pera(ANCHO_CELDAS, ALTO_CELDAS)
ciruela = Ciruela(ANCHO_CELDAS, ALTO_CELDAS)
powerup = PowerupCongelar(ANCHO_CELDAS, ALTO_CELDAS)
obstaculos = [(o.x, o.y) for o in [Obstaculo(ANCHO_CELDAS, ALTO_CELDAS, TAM_CELDA) for _ in range(5)]]

duplicar_puntaje = {"jugador1": False, "jugador2": False}
tiempo_duplicar = {"jugador1": 0, "jugador2": 0}
congelado = False
tiempo_congelado = 0
DURACION_POWERUP = 10000
