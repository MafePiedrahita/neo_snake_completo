#Clase jugador para multijugador Mariana
from serpiente import Serpiente

class Jugador:
    def __init__(self, teclas, color):
        self.serpiente = Serpiente()
        self.teclas = teclas
        self.color = color
        self.puntaje = 0

    def controlar(self, evento):
        if evento.key == self.teclas.get("UP"):
            self.serpiente.cambiar_direccion("ARRIBA")
        elif evento.key == self.teclas.get("DOWN"):
            self.serpiente.cambiar_direccion("ABAJO")
        elif evento.key == self.teclas.get("LEFT"):
            self.serpiente.cambiar_direccion("IZQUIERDA")
        elif evento.key == self.teclas.get("RIGHT"):
            self.serpiente.cambiar_direccion("DERECHA")