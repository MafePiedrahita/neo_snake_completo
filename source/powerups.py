import random

TAM_CELDA = 50

class PowerupCongelar:
    def __init__(self, ancho_tablero, alto_tablero, recursos):
        self.x = random.randint(0, ancho_tablero - 1)
        self.y = random.randint(0, alto_tablero - 1)
        self.visible = True
        self.imagen = recursos.get_imagen("powerup_congelar")

    def dibujar(self, superficie):
        if self.visible and self.imagen:
            superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

    def activar(self):
        self.visible = False

    def obtener_posicion(self):
        return (self.x, self.y)