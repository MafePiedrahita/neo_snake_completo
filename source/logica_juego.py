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

def actualizar_estado(jugadores, peras, ciruelas, powerup, obstaculos,
                      duplicar_puntaje, tiempo_duplicar,
                      tiempo_congelado, congelado, tiempo_actual, DURACION_POWERUP,
                      ancho_celdas, alto_celdas, inicio_juego, TIEMPO_GRACIA):

    en_tiempo_de_gracia = tiempo_actual - inicio_juego < TIEMPO_GRACIA

    for nombre, jugador in jugadores.items():
        jugador.serpiente.mover()
        cabeza = jugador.serpiente.cabeza.posicion

        # Comer peras
        for pera in peras:
            if cabeza == (pera.x, pera.y):
                jugador.serpiente.crecer()
                pera.nueva_posicion()
                jugador.puntaje += 2 if duplicar_puntaje[nombre] else 1

        # Comer ciruelas
        for ciruela in ciruelas:
            if cabeza == (ciruela.x, ciruela.y):
                jugador.serpiente.crecer()
                ciruela.nueva_posicion()
                duplicar_puntaje[nombre] = True
                tiempo_duplicar[nombre] = tiempo_actual

        # Tocar powerup de congelar
        if powerup.visible and cabeza == (powerup.x, powerup.y):
            powerup.activar()
            congelado = True
            tiempo_congelado = tiempo_actual

        # Colisión
        if not en_tiempo_de_gracia and jugador.serpiente.colisionar(ancho_celdas, alto_celdas, obstaculos):
            print(f"{nombre} colisionó en {jugador.serpiente.cabeza.posicion}")
            guardar_puntaje(nombre, jugador.puntaje)
            return False, congelado, tiempo_congelado

    # Finaliza efecto de congelar si ha pasado el tiempo
    if congelado and tiempo_actual - tiempo_congelado > DURACION_POWERUP:
        congelado = False

    return True, congelado, tiempo_congelado

