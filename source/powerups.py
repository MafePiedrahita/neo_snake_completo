from source.utils import generar_posicion_libre

TAM_CELDA = 50

# === POWER-UP CONGELAR ===
class PowerupCongelar:
    def __init__(self, ancho_tablero, alto_tablero, recursos, posiciones_ocupadas):
        self.x, self.y = generar_posicion_libre(ancho_tablero, alto_tablero, posiciones_ocupadas)
        self.visible = True
        self.imagen = recursos.get_imagen("powerup_congelar")

    def dibujar(self, superficie):
        if self.visible and self.imagen:
            superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

    def activar(self):
        self.visible = False

    def obtener_posicion(self):
        return (self.x, self.y)

# === POWER-UP INMORTALIDAD ===
class PowerupInmortalidad:
    def __init__(self, ancho_tablero, alto_tablero, recursos, posiciones_ocupadas):
        self.x, self.y = generar_posicion_libre(ancho_tablero,alto_tablero, posiciones_ocupadas)
        self.visible = True
        self.imagen = recursos.get_imagen("powerup_inmortalidad")
        self.duracion = 300  # duración en ticks

    def dibujar(self, superficie):
        if self.visible and self.imagen:
            superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

    def activar(self, jugador):
        self.visible = False
        jugador.inmortal = True
        jugador.tiempo_inmortal = self.duracion

    def obtener_posicion(self):
        return (self.x, self.y)

# === POWER-UP CAMBIO ALEATORIO DE DIRECCIÓN ===
class PowerupCambioAleatorio:
    def __init__(self, ancho_tablero, alto_tablero, recursos, posiciones_ocupadas):
        self.x, self.y = generar_posicion_libre(ancho_tablero, alto_tablero, posiciones_ocupadas)
        self.visible = True
        self.imagen = recursos.get_imagen("powerup_random")

    def dibujar(self, superficie):
        if self.visible and self.imagen:
            superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

    def activar(self, jugador):
        self.visible = False
        direcciones = ["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"]
        opuesta = jugador.serpiente.direccion_opuesta()
        if opuesta in direcciones:
            direcciones.remove(opuesta)
        nueva = random.choice(direcciones)
        jugador.serpiente.cambiar_direccion(nueva)

    def obtener_posicion(self):
        return (self.x, self.y)

# === POWER-UP IMÁN ===
class PowerupIman:
    def __init__(self, ancho_tablero, alto_tablero, recursos, posiciones_ocupadas):
        self.x, self.y = generar_posicion_libre(ancho_tablero, alto_tablero, posiciones_ocupadas)
        self.visible = True
        self.imagen = recursos.get_imagen("powerup_iman")
        self.rango = 3  # rango de atracción

    def dibujar(self, superficie):
        if self.visible and self.imagen:
            superficie.blit(self.imagen, (self.x * TAM_CELDA, self.y * TAM_CELDA))

    def activar(self, jugador):
        self.visible = False
        jugador.iman_activo = True
        jugador.rango_iman = self.rango

    def obtener_posicion(self):
        return (self.x, self.y)
