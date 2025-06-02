import random

def generar_posicion_libre(ancho, alto, posiciones_ocupadas):
    intentos = 0
    while True:
        x = random.randint(0, ancho - 1)
        y = random.randint(0, alto - 1)
        if (x, y) not in posiciones_ocupadas:
            return x, y
        intentos += 1
        if intentos > 1000:
            raise Exception("No se pudo encontrar una posición libre.")
