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

    def cambiar_direccion(self, nueva_direccion):
        opuestos = {"ARRIBA": "ABAJO", "ABAJO": "ARRIBA", "IZQUIERDA": "DERECHA", "DERECHA": "IZQUIERDA"}
        if nueva_direccion != opuestos.get(self.direccion, None):
            self.direccion = nueva_direccion

class Cuerpo:
    def __init__(self):
        self.segmentos = []

    def mover(self, nueva_posicion):
        self.segmentos.insert(0, nueva_posicion)
        if len(self.segmentos) > 1:
                self.segmentos.pop()

    def crecer(self):
            if self.segmentos:
                self.segmentos.append(self.segmentos[-1])

class Cola:
    def __init__(self):
        self.posicion = None

    def actualizar(self, nueva_posicion):
        self.posicion = nueva_posicion
