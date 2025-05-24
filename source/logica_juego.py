import pygame
from puntajes import guardar_puntaje

def manejar_eventos(jugador1, jugador2):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        elif evento.type == pygame.KEYDOWN:
            jugador1.controlar(evento)
            jugador2.controlar(evento)
    return True