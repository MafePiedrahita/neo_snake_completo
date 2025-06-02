import pygame
from puntajes import guardar_puntaje
from source.powerups import PowerupCongelar, PowerupInmortalidad, PowerupCambioAleatorio, PowerupIman

def manejar_eventos(jugador1, jugador2):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        elif evento.type == pygame.KEYDOWN:
            jugador1.controlar(evento)
            jugador2.controlar(evento)
    return True

def actualizar_estado(jugadores, peras, ciruelas, powerups, obstaculos,
                      duplicar_puntaje, tiempo_duplicar,
                      tiempo_congelado, congelado, tiempo_actual, DURACION_POWERUP,
                      ancho_celdas, alto_celdas, inicio_juego, TIEMPO_GRACIA):

    en_tiempo_de_gracia = False  # Puedes usar esto más adelante si quieres revivir con delay

    for nombre, jugador in jugadores.items():
        jugador.serpiente.mover()
        cabeza = jugador.serpiente.cabeza.posicion

        # === ACTIVAR POWER-UPS primero ===
        for powerup in powerups:
            if powerup.visible and cabeza == powerup.obtener_posicion():
                try:
                    powerup.activar(jugador)  # Si requiere jugador
                except TypeError:
                    powerup.activar()         # Si no lo requiere

                if isinstance(powerup, PowerupCongelar):
                    congelado = True
                    tiempo_congelado = tiempo_actual

        # === Comer peras ===
        for pera in peras:
            if cabeza == (pera.x, pera.y):
                jugador.serpiente.crecer()
                pera.nueva_posicion()
                jugador.puntaje += 2 if duplicar_puntaje[nombre] else 1

        # === Comer ciruelas ===
        for ciruela in ciruelas:
            if cabeza == (ciruela.x, ciruela.y):
                jugador.serpiente.crecer()
                ciruela.nueva_posicion()
                duplicar_puntaje[nombre] = True
                tiempo_duplicar[nombre] = tiempo_actual

        # === Evaluar colisiones si NO es inmortal ===
        if not en_tiempo_de_gracia and not getattr(jugador, "inmortal", False):
            if jugador.serpiente.colisionar(ancho_celdas, alto_celdas, obstaculos):
                print(f"{nombre} colisionó con borde, cuerpo o obstáculo en {jugador.serpiente.cabeza.posicion}")
                guardar_puntaje(nombre, jugador.puntaje)
                return False, congelado, tiempo_congelado

            for otro_nombre, otro_jugador in jugadores.items():
                if nombre != otro_nombre:
                    if cabeza in otro_jugador.serpiente.cuerpo.segmentos:
                        print(f"{nombre} colisionó con el cuerpo de {otro_nombre}")
                        guardar_puntaje(nombre, jugador.puntaje)
                        return False, congelado, tiempo_congelado

    # === Finaliza efecto de duplicar puntaje ===
    for nombre in jugadores:
        if duplicar_puntaje[nombre] and tiempo_actual - tiempo_duplicar[nombre] > DURACION_POWERUP:
            duplicar_puntaje[nombre] = False

    # === Finaliza efecto de congelar ===
    if congelado and tiempo_actual - tiempo_congelado > DURACION_POWERUP:
        congelado = False

    # === Finaliza efectos por jugador ===
    for jugador in jugadores.values():
        if getattr(jugador, "inmortal", False) and tiempo_actual - jugador.tiempo_inmortal > DURACION_POWERUP:
            jugador.inmortal = False
        if getattr(jugador, "iman_activo", False) and tiempo_actual - jugador.tiempo_iman > DURACION_POWERUP:
            jugador.iman_activo = False

    return True, congelado, tiempo_congelado
