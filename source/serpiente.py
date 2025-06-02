import pygame

TAM_CELDA = 50

class Cabeza:
    def __init__(self, x, y, imagen):
        self.posicion = (x, y)
        self.direccion = "DERECHA"
        self.imagen_base = imagen
        self.imagen = imagen
        self.rotar_imagen()

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
            self.rotar_imagen()

    def rotar_imagen(self):
        if self.direccion == "ARRIBA":
            self.imagen = pygame.transform.rotate(self.imagen_base, 90)
        elif self.direccion == "ABAJO":
            self.imagen = pygame.transform.rotate(self.imagen_base, -90)
        elif self.direccion == "IZQUIERDA":
            self.imagen = pygame.transform.rotate(self.imagen_base, 180)
        elif self.direccion == "DERECHA":
            self.imagen = self.imagen_base

    def direccion_opuesta(self):
        opuestos = {
            "ARRIBA": "ABAJO",
            "ABAJO": "ARRIBA",
            "IZQUIERDA": "DERECHA",
            "DERECHA": "IZQUIERDA"
        }
        return opuestos[self.direccion]


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
        self.imagen_base = imagen
        self.imagen = imagen

    def actualizar(self, nueva_posicion, direccion="DERECHA"):
        self.posicion = nueva_posicion
        self.rotar_imagen(direccion)

    def rotar_imagen(self, direccion):
        if direccion == "ARRIBA":
            self.imagen = pygame.transform.rotate(self.imagen_base, 90)
        elif direccion == "ABAJO":
            self.imagen = pygame.transform.rotate(self.imagen_base, -90)
        elif direccion == "IZQUIERDA":
            self.imagen = pygame.transform.rotate(self.imagen_base, 180)
        elif direccion == "DERECHA":
            self.imagen = self.imagen_base


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

        if len(self.cuerpo.segmentos) >= 1:
            ultima = self.cuerpo.segmentos[-1]
            anteultima = self.cuerpo.segmentos[-2] if len(self.cuerpo.segmentos) >= 2 else self.cabeza.posicion
            dx = anteultima[0] - ultima[0]
            dy = anteultima[1] - ultima[1]

            if dx == 1:
                direccion = "DERECHA"
            elif dx == -1:
                direccion = "IZQUIERDA"
            elif dy == 1:
                direccion = "ABAJO"
            elif dy == -1:
                direccion = "ARRIBA"
            else:
                direccion = "DERECHA"

            self.cola.actualizar(ultima, direccion)

    def cambiar_direccion(self, nueva_direccion):
        self.cabeza.cambiar_direccion(nueva_direccion)

    def crecer(self):
        self.longitud += 1
        self.cuerpo.crecer()

    def obtener_posiciones(self):
        return [self.cabeza.posicion] + self.cuerpo.segmentos

    def obtener_cabeza(self):
        return self.cabeza.posicion

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
