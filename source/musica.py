#Reproducción de música con pygame.mixer
from pathlib import Path
import pygame.mixer

def cargar_musica(ruta_relativa):
    pygame.mixer.init()
    base_dir = Path(__file__).resolve().parent
    ruta_completa = (base_dir / ".." / ruta_relativa).resolve()
    pygame.mixer.music.load(str(ruta_completa))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def detener_musica():
    pygame.mixer.music.stop()

