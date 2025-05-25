#Clase jugador para multijugador Mariana
from source.serpiente import Serpiente

class Jugador:
    def __init__(self, teclas, color, posicion_inicial, recursos):
        self.teclas = teclas
        self.color = color
        self.puntaje = 0
        x, y = posicion_inicial
        self.serpiente = Serpiente(x, y, recursos)

    def controlar(self, evento):
        if evento.key == self.teclas["UP"]:
            self.serpiente.cambiar_direccion("ARRIBA")
        elif evento.key == self.teclas["DOWN"]:
            self.serpiente.cambiar_direccion("ABAJO")
        elif evento.key == self.teclas["LEFT"]:
            self.serpiente.cambiar_direccion("IZQUIERDA")
        elif evento.key == self.teclas["RIGHT"]:
            self.serpiente.cambiar_direccion("DERECHA")
