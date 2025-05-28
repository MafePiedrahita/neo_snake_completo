#Clase jugador para multijugador Mariana
from source.serpiente import Serpiente

class Jugador:
    def __init__(self, teclas, color, posicion_inicial, recursos, jugador_id):
        self.teclas = teclas
        self.color = color
        self.puntaje = 0
        x, y = posicion_inicial
        self.serpiente = Serpiente(x, y, recursos, jugador_id)

    def controlar(self, evento):
        if evento.key == self.teclas["ARRIBA"]:
            self.serpiente.cambiar_direccion("ARRIBA")
        elif evento.key == self.teclas["ABAJO"]:
            self.serpiente.cambiar_direccion("ABAJO")
        elif evento.key == self.teclas["IZQUIERDA"]:
            self.serpiente.cambiar_direccion("IZQUIERDA")
        elif evento.key == self.teclas["DERECHA"]:
            self.serpiente.cambiar_direccion("DERECHA")
