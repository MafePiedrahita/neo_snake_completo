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

def actualizar_estado(jugadores, pera, ciruela, powerup, osbtaculos,
                      duplicar_puntaje, tiempo_duplicar, tiempo_congelado,
                      congelado, tiempo_actual, DURACION_POWERUP
                      ):
    for nombre, jugador in jugadores.items():
        jugador.serpiente.mover()
        cabeza = jugador.serpiente.cabeza.posicion

        #comer pera
        if cabeza == (pera.x, pera.y):
            jugador.serpiente.crecer()
            pera.nueva_posicion()
            jugador.puntaje += 2 if duplicar_puntaje[nombre] else 1

        #comer ciruela accion powerup
        if cabeza == (ciruela.x, ciruela.y):
            jugador.serpiente.crecer()
            ciruela.nueva_posicion()
            duplicar_puntaje[nombre] = True
            tiempo_duplicar[nombre] = tiempo_actual

        #tocar el congelar
        if powerup.visible and cabeza == (powerup.x, powerup.y):
            powerup.activar()
            congelado = True
            tiempo_congelado = tiempo_actual

        #colsion obstaculo, cuerpo / borde
        if jugador.serpiente.colisionar(obstaculos=osbtaculos):
            print(f"{nombre} colisionaste:(!!")
            guardar_puntaje(nombre, jugador.puntaje)
            return False, congelado, tiempo_congelado

        #finaliza congelado
        if congelado and tiempo_actual - tiempo_congelado > DURACION_POWERUP:
            congelado = False

        return True, congelado, tiempo_congelado

