# Clase jugador para multijugador Mariana
from source.serpiente import Serpiente

class Jugador:
    def __init__(self, teclas, color, posicion_inicial, recursos, jugador_id):
        self.teclas = teclas
        self.color = color
        self.puntaje = 0
        x, y = posicion_inicial
        self.serpiente = Serpiente(x, y, recursos, jugador_id)

        # === POWER-UPS ===
        self.inmortal = False
        self.tiempo_inmortal = 0

        self.iman_activo = False
        self.rango_iman = 0

    def controlar(self, evento):
        if evento.key == self.teclas["ARRIBA"]:
            self.serpiente.cambiar_direccion("ARRIBA")
        elif evento.key == self.teclas["ABAJO"]:
            self.serpiente.cambiar_direccion("ABAJO")
        elif evento.key == self.teclas["IZQUIERDA"]:
            self.serpiente.cambiar_direccion("IZQUIERDA")
        elif evento.key == self.teclas["DERECHA"]:
            self.serpiente.cambiar_direccion("DERECHA")

    def actualizar_powerups(self):
        # Inmortalidad
        if self.inmortal:
            self.tiempo_inmortal -= 1
            if self.tiempo_inmortal <= 0:
                self.inmortal = False

        # Imán
        # El efecto se usa desde el juego cuando se mueven frutas
