#Reproducción de música con pygame.mixer
from pathlib import Path
import pygame.mixer
from source.recursos import Recursos


def cargar_musica():
    pygame.mixer.init()
    recursos = Recursos()
    ruta_relativa = recursos.get_sonido("musica_fondo")

    ruta_completa = Path(__file__).resolve().parent / ruta_relativa

    if not ruta_completa.exists():
        raise FileNotFoundError(f"Archivo de música no encontrado: {ruta_completa}")

    pygame.mixer.music.load(str(ruta_completa))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


def detener_musica():
    pygame.mixer.music.stop()
