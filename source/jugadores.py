# Clase jugador para multijugador Mariana
from source.serpiente import Serpiente
import pygame

class Jugador:
    def __init__(self, teclas, color, posicion_inicial, recursos, jugador_id):
        self.teclas = teclas
        self.color = color
        self.puntaje = 0
        x, y = posicion_inicial
        self.serpiente = Serpiente(x, y, recursos, jugador_id)

        # Atributos para power-ups
        self.inmortal = False
        self.tiempo_inmortal = 0
        self.iman_activo = False
        self.tiempo_iman = 0
        self.congelado = False
        self.tiempo_congelado = 0

    def controlar(self, evento):
        if evento.key == self.teclas["ARRIBA"]:
            self.serpiente.cambiar_direccion("ARRIBA")
        elif evento.key == self.teclas["ABAJO"]:
            self.serpiente.cambiar_direccion("ABAJO")
        elif evento.key == self.teclas["IZQUIERDA"]:
            self.serpiente.cambiar_direccion("IZQUIERDA")
        elif evento.key == self.teclas["DERECHA"]:
            self.serpiente.cambiar_direccion("DERECHA")

    def actualizar_powerups(self, tiempo_actual, DURACION_POWERUP):
        # Inmortalidad
        if self.inmortal and tiempo_actual - self.tiempo_inmortal > DURACION_POWERUP:
            self.inmortal = False

        # Imán
        if self.iman_activo and tiempo_actual - self.tiempo_iman > DURACION_POWERUP:
            self.iman_activo = False

        # Congelado
        if self.congelado and tiempo_actual - self.tiempo_congelado > DURACION_POWERUP:
            self.congelado = False
