import pygame
import sys
from source.recursos import Recursos
from source.alimentos import Pera, Ciruela
from source.obstaculos import Obstaculo
from source.powerups import PowerupCongelar
from source.musica import cargar_musica, detener_musica
from source.puntajes import mostrar_puntajes
from source.jugadores import Jugador
from source.logica_juego import manejar_eventos, actualizar_estado

# Inicializar pygame y recursos
pygame.init()
recursos = Recursos()
cargar_musica()

# Constantes
TAM_CELDA = 50
ANCHO, ALTO = 1000, 1000
FPS = 10
ANCHO_CELDAS = ANCHO // TAM_CELDA
ALTO_CELDAS = ALTO // TAM_CELDA

# Colores
NEGRO = (0, 0, 0)
BLANCO = (225, 225, 0)
AMARILLO = (255, 255, 0)
verde = (0, 128, 0)
ROJO = (255, 0, 0)

# Pantalla y reloj
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Neo-Snake Multijugador")
clock = pygame.time.Clock()

# Jugadores
jugador1 = Jugador({
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT
}, verde, (5, 5), recursos)

jugador2 = Jugador({
    "UP": pygame.K_w,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d
}, ROJO, (15, 15), recursos)

jugadores = {
    "jugador1": jugador1,
    "jugador2": jugador2
}

# Elementos del juego
pera = Pera(ANCHO_CELDAS, ALTO_CELDAS, recursos)
ciruela = Ciruela(ANCHO_CELDAS, ALTO_CELDAS, recursos)
powerup = PowerupCongelar(ANCHO_CELDAS, ALTO_CELDAS)
obstaculos = [(o.x, o.y) for o in [Obstaculo(ANCHO_CELDAS, ALTO_CELDAS, recursos) for _ in range(5)]]

duplicar_puntaje = {"jugador1": False, "jugador2": False}
tiempo_duplicar = {"jugador1": 0, "jugador2": 0}
congelado = False
tiempo_congelado = 0
DURACION_POWERUP = 10000

# Fondo
tabla_fondo = recursos.get_imagen("fondo_tablero")
tabla_fondo = pygame.transform.scale(tabla_fondo, (ANCHO, ALTO))

# Bucle principal
corriendo = True
while corriendo:
    tiempo_actual = pygame.time.get_ticks()
    clock.tick(3 if congelado else FPS)
    pantalla.blit(tabla_fondo, (0, 0))

    # Manejar eventos
    corriendo = manejar_eventos(jugador1, jugador2)
    if not corriendo:
        break

    # Actualizar estado del juego
    corriendo, congelado, tiempo_congelado = actualizar_estado(
        jugadores, pera, ciruela, powerup, obstaculos,
        duplicar_puntaje, tiempo_duplicar,
        tiempo_congelado, congelado, tiempo_actual, DURACION_POWERUP,
        ANCHO_CELDAS, ALTO_CELDAS
    )

    # Dibujar serpientes
    for nombre, jugador in jugadores.items():
        x, y = jugador.serpiente.cabeza.posicion
        pantalla.blit(jugador.serpiente.cabeza.imagen, (x * TAM_CELDA, y * TAM_CELDA))

        for x, y in jugador.serpiente.cuerpo.segmentos:
            pantalla.blit(jugador.serpiente.cuerpo.imagen, (x * TAM_CELDA, y * TAM_CELDA))

    # Dibujar obstáculos
    for x, y in obstaculos:
        pantalla.blit(recursos.get_imagen("obstaculo"), (x * TAM_CELDA, y * TAM_CELDA))

    # Dibujar frutas y powerups
    pera.dibujar(pantalla)
    ciruela.dibujar(pantalla)
    powerup.dibujar(pantalla)

    # Dibujar puntajes
    fuente = pygame.font.SysFont(None, 28)
    texto1 = fuente.render(f"P1: {jugador1.puntaje}", True, BLANCO)
    texto2 = fuente.render(f"P2: {jugador2.puntaje}", True, BLANCO)
    pantalla.blit(texto1, (10, 10))
    pantalla.blit(texto2, (10, 40))

    pygame.display.flip()

# Finalizar
pygame.quit()
detener_musica()
mostrar_puntajes()
sys.exit()
