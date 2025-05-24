#Reproducción de música con pygame.mixer
import pygame.mixer

def cargar_musica(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

