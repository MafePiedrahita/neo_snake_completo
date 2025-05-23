#Clase jugador para multijugador Mariana
from serpiente import Serpiente

class Jugador:
    def __init__(self, teclas, color):
        self.serpiente = Serpiente()
        self.teclas = teclas
        self.color = color
        self.puntaje = 0
