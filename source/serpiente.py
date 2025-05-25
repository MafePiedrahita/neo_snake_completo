#Clases de la serpiente (Cabeza, Cuerpo, Cola) Mariana
import pygame

TAM_CELDA = 50

class Cabeza:
    def __init__(self, x, y, recursos):
        self.posicion = (x, y)
        self.direccion = "DERECHA"
        self.imagen = recursos.get_imagen("cabeza")

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
    def __init__(self, recursos):
        self.segmentos = []
        self.imagen = recursos.get_imagen("cuerpo")

    def mover(self, nueva_posicion):
        self.segmentos.insert(0, nueva_posicion)
        if len(self.segmentos) > 1:
            self.segmentos.pop()

    def crecer(self):
        if self.segmentos:
            self.segmentos.append(self.segmentos[-1])


class Cola:
    def __init__(self, recursos):
        self.posicion = None
        self.imagen = recursos.get_imagen("cola")

    def actualizar(self, nueva_posicion):
        self.posicion = nueva_posicion


class Serpiente:
    def __init__(self, x_inicial=5, y_inicial=5, recursos=None):
        self.cabeza = Cabeza(x_inicial, y_inicial, recursos)
        self.cuerpo = Cuerpo(recursos)
        self.cola = Cola(recursos)
        self.longitud = 1

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
