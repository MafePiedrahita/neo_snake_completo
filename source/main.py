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
pygame.font.init()
recursos = Recursos()
cargar_musica()

# Constantes
TAM_CELDA = 50
ANCHO, ALTO = 1000, 1000
ANCHO_CELDAS = ANCHO // TAM_CELDA
ALTO_CELDAS = ALTO // TAM_CELDA

# Colores
NEGRO = (0, 0, 0)
BLANCO = (225, 225, 0)
AMARILLO = (255, 255, 0)
verde = (0, 128, 0)
ROJO = (255, 0, 0)
AZUL_OSCURO = (30, 30, 60)
AZUL_CLARO = (100, 149, 237)
GRIS_SUAVE = (200, 200, 200)

# Pantalla y reloj
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Neo-Snake Multijugador")
clock = pygame.time.Clock()

def mostrar_menu_dificultad(pantalla):
    pygame.mouse.set_visible(True)
    fuente = pygame.font.SysFont("Arial", 36, bold=True)
    titulo_font = pygame.font.SysFont("Arial", 60, bold=True)

    opciones = [
        ("Fácil",     {"fps": 5,  "obstaculos": 3,  "powerup_duracion": 15000, "tiempo_gracia": 5000, "frutas": 1}),
        ("Intermedio", {"fps": 10, "obstaculos": 5,  "powerup_duracion": 10000, "tiempo_gracia": 5000, "frutas": 2}),
        ("Difícil",    {"fps": 15, "obstaculos": 7,  "powerup_duracion": 7000,  "tiempo_gracia": 3000, "frutas": 3}),
        ("Extremo",    {"fps": 20, "obstaculos": 10, "powerup_duracion": 5000,  "tiempo_gracia": 2000, "frutas": 4}),
    ]

    botones = []
    for i, (texto, config) in enumerate(opciones):
        rect = pygame.Rect(350, 250 + i * 100, 300, 70)
        botones.append((rect, texto, config))

    seleccion = None
    while seleccion is None:
        pantalla.fill(AZUL_OSCURO)
        titulo = titulo_font.render("Selecciona dificultad", True, GRIS_SUAVE)
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

        mouse_pos = pygame.mouse.get_pos()

        for rect, texto, _ in botones:
            color = AZUL_CLARO if rect.collidepoint(mouse_pos) else (60, 60, 90)
            pygame.draw.rect(pantalla, color, rect, border_radius=12)
            pygame.draw.rect(pantalla, GRIS_SUAVE, rect, width=2, border_radius=12)

            texto_render = fuente.render(texto, True, (255, 255, 255))
            pantalla.blit(
                texto_render,
                (
                    rect.x + (rect.width - texto_render.get_width()) // 2,
                    rect.y + (rect.height - texto_render.get_height()) // 2
                )
            )

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for rect, _, config in botones:
                    if rect.collidepoint(evento.pos):
                        seleccion = config

    return seleccion

def mostrar_menu_final(pantalla, puntaje1, puntaje2):
    pygame.mouse.set_visible(True)
    fuente_boton = pygame.font.SysFont("Arial", 36, bold=True)
    fuente_titulo = pygame.font.SysFont("Arial", 64, bold=True)
    fuente_puntaje = pygame.font.SysFont("Arial", 40, bold=True)

    opciones = ["Reiniciar", "Elegir de nuevo", "Salir"]
    botones = []
    ancho_ventana, alto_ventana = pantalla.get_size()

    for i, texto in enumerate(opciones):
        rect = pygame.Rect(ancho_ventana // 2 - 180, 270 + i * 110, 360, 70)
        botones.append((rect, texto))

    seleccion = None
    while seleccion is None:
        pantalla.fill((20, 20, 50))
        titulo = fuente_titulo.render("Perdieron :(", True, (255, 80, 80))
        pantalla.blit(titulo, (ancho_ventana // 2 - titulo.get_width() // 2, 60))

        texto_p1 = fuente_puntaje.render(f"Puntaje Jugador 1: {puntaje1}", True, (255, 255, 255))
        texto_p2 = fuente_puntaje.render(f"Puntaje Jugador 2: {puntaje2}", True, (255, 255, 255))
        pantalla.blit(texto_p1, (ancho_ventana // 2 - texto_p1.get_width() // 2, 150))
        pantalla.blit(texto_p2, (ancho_ventana // 2 - texto_p2.get_width() // 2, 200))

        mouse_pos = pygame.mouse.get_pos()
        for rect, texto in botones:
            hover = rect.collidepoint(mouse_pos)
            color_fondo = (230, 230, 230) if hover else (60, 60, 90)
            color_borde = (255, 255, 255)
            color_texto = (0, 0, 0) if hover else (255, 255, 255)
            pygame.draw.rect(pantalla, color_fondo, rect, border_radius=20)
            pygame.draw.rect(pantalla, color_borde, rect, width=2, border_radius=20)
            texto_render = fuente_boton.render(texto, True, color_texto)
            pantalla.blit(
                texto_render,
                (
                    rect.x + (rect.width - texto_render.get_width()) // 2,
                    rect.y + (rect.height - texto_render.get_height()) // 2
                )
            )

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for i, (rect, _) in enumerate(botones):
                    if rect.collidepoint(evento.pos):
                        seleccion = i

    return seleccion

def jugar(config):
    FPS = config["fps"]
    DURACION_POWERUP = config["powerup_duracion"]
    TIEMPO_GRACIA = config["tiempo_gracia"]

    teclas_jugador1 = {"ARRIBA": pygame.K_UP, "ABAJO": pygame.K_DOWN, "IZQUIERDA": pygame.K_LEFT, "DERECHA": pygame.K_RIGHT}
    teclas_jugador2 = {"ARRIBA": pygame.K_w, "ABAJO": pygame.K_s, "IZQUIERDA": pygame.K_a, "DERECHA": pygame.K_d}

    jugador1 = Jugador(teclas_jugador1, verde, (7, 8), recursos, "j1")
    jugador2 = Jugador(teclas_jugador2, ROJO, (11, 10), recursos, "j2")
    jugadores = {"jugador1": jugador1, "jugador2": jugador2}

    num_frutas = config["frutas"]
    peras = [Pera(ANCHO_CELDAS, ALTO_CELDAS, recursos) for _ in range(num_frutas)]
    ciruelas = [Ciruela(ANCHO_CELDAS, ALTO_CELDAS, recursos) for _ in range(num_frutas)]
    powerup = PowerupCongelar(ANCHO_CELDAS, ALTO_CELDAS)

    posiciones_prohibidas = [(9, 10), (11, 10)]
    obstaculos = []
    while len(obstaculos) < config["obstaculos"]:
        nuevo = Obstaculo(ANCHO_CELDAS, ALTO_CELDAS, recursos)
        if (nuevo.x, nuevo.y) not in posiciones_prohibidas:
            obstaculos.append((nuevo.x, nuevo.y))

    duplicar_puntaje = {"jugador1": False, "jugador2": False}
    tiempo_duplicar = {"jugador1": 0, "jugador2": 0}
    congelado = False
    tiempo_congelado = 0
    inicio_juego = pygame.time.get_ticks()

    tabla_fondo = recursos.get_imagen("fondo_tablero")
    tabla_fondo = pygame.transform.scale(tabla_fondo, (ANCHO, ALTO))
    cargar_musica()

    corriendo = True
    while corriendo:
        tiempo_actual = pygame.time.get_ticks()
        clock.tick(3 if congelado else FPS)
        pantalla.blit(tabla_fondo, (0, 0))

        corriendo = manejar_eventos(jugador1, jugador2)
        if not corriendo:
            break

        corriendo, congelado, tiempo_congelado = actualizar_estado(
            jugadores, peras, ciruelas, powerup, obstaculos,
            duplicar_puntaje, tiempo_duplicar,
            tiempo_congelado, congelado, tiempo_actual, DURACION_POWERUP,
            ANCHO_CELDAS, ALTO_CELDAS, inicio_juego, TIEMPO_GRACIA
        )

        for jugador in jugadores.values():
            if jugador.serpiente.colisionar(ANCHO_CELDAS, ALTO_CELDAS, obstaculos):
                corriendo = False
                break

        for nombre, jugador in jugadores.items():
            x, y = jugador.serpiente.cabeza.posicion
            pantalla.blit(jugador.serpiente.cabeza.imagen, (x * TAM_CELDA, y * TAM_CELDA))
            for x, y in jugador.serpiente.cuerpo.segmentos:
                pantalla.blit(jugador.serpiente.cuerpo.imagen, (x * TAM_CELDA, y * TAM_CELDA))

        for x, y in obstaculos:
            pantalla.blit(recursos.get_imagen("obstaculo"), (x * TAM_CELDA, y * TAM_CELDA))

        for pera in peras:
            pera.dibujar(pantalla)

        for ciruela in ciruelas:
            ciruela.dibujar(pantalla)

        powerup.dibujar(pantalla)

        fuente = pygame.font.SysFont(None, 28)
        texto1 = fuente.render(f"P1: {jugador1.puntaje}", True, BLANCO)
        texto2 = fuente.render(f"P2: {jugador2.puntaje}", True, BLANCO)
        pantalla.blit(texto1, (10, 10))
        pantalla.blit(texto2, (10, 40))

        pygame.display.flip()

    detener_musica()
    mostrar_puntajes()
    return jugador1.puntaje, jugador2.puntaje

# Bucle principal
config = None
while True:
    if config is None:
        config = mostrar_menu_dificultad(pantalla)

    puntaje1, puntaje2 = jugar(config)

    eleccion = mostrar_menu_final(pantalla, puntaje1, puntaje2)

    if eleccion == 0:
        continue
    elif eleccion == 1:
        config = None
        continue
    elif eleccion == 2:
        pygame.quit()
        sys.exit()