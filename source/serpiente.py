#Clases de la serpiente (Cabeza, Cuerpo, Cola) Mariana
TAM_CELDA = 50

class Cabeza:
    def __init__(self, x, y, imagen):
        self.posicion = (x, y)
        self.direccion = "DERECHA"
        self.imagen = imagen

    def mover(self):
        x, y = self.posicion
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
        opuestos = {
            "ARRIBA": "ABAJO",
            "ABAJO": "ARRIBA",
            "IZQUIERDA": "DERECHA",
            "DERECHA": "IZQUIERDA"
        }
        if nueva_direccion != opuestos.get(self.direccion):
            self.direccion = nueva_direccion


class Cuerpo:
    def __init__(self, imagen):
        self.segmentos = []
        self.imagen = imagen

    def mover(self, nueva_posicion):
        self.segmentos.insert(0, nueva_posicion)
        if len(self.segmentos) > 1:
            self.segmentos.pop()

    def crecer(self):
        if self.segmentos:
            self.segmentos.append(self.segmentos[-1])


class Cola:
    def __init__(self, imagen):
        self.posicion = None
        self.imagen = imagen

    def actualizar(self, nueva_posicion):
        self.posicion = nueva_posicion


class Serpiente:
    def __init__(self, x, y, recursos, jugador_id):
        self.cabeza = Cabeza(x, y, recursos.get_imagen(f"cabeza_{jugador_id}"))
        self.cuerpo = Cuerpo(recursos.get_imagen(f"cuerpo_{jugador_id}"))
        self.cola = Cola(recursos.get_imagen(f"cola_{jugador_id}"))
        self.longitud = 3

    def mover(self):
        pos_anterior = self.cabeza.posicion
        self.cabeza.mover()
        self.cuerpo.mover(pos_anterior)
        if len(self.cuerpo.segmentos) == self.longitud - 1 and self.cuerpo.segmentos:
            self.cola.actualizar(self.cuerpo.segmentos[-1])

    def cambiar_direccion(self, nueva_direccion):
        self.cabeza.cambiar_direccion(nueva_direccion)

    def crecer(self):
        self.longitud += 1
        self.cuerpo.crecer()

    def obtener_posiciones(self):
        return [self.cabeza.posicion] + self.cuerpo.segmentos

    def colisionar(self, ancho_celdas, alto_celdas, obstaculos=None):
        if obstaculos is None:
            obstaculos = []

        x, y = self.cabeza.posicion

        if not (0 <= x < ancho_celdas and 0 <= y < alto_celdas):
            return True

        if self.cabeza.posicion in self.cuerpo.segmentos:
            return True

        if self.cabeza.posicion in obstaculos:
            return True

        return False
