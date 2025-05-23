#Clases de la serpiente (Cabeza, Cuerpo, Cola) Mariana
class Cabeza:
    def __init__(self, x,y):
        self.posicion = (x, y)
        self.direccion = "DERECHA"

    def mover(self):
        x,y = self.posicion
        if self.direccion == "ARRIBA":
            y -= 1
        elif self.direccion == "ABAJO":
            y += 1
        elif self.direccion == "IZQUIERDA":
            x -= 1
        elif self.direccion == "DERECHA":
            x += 1
        self.posicion = (x, y)