import pygame
from source.config_loader import ConfigLoader

class Recursos:
    def __init__(self):
        self.config = ConfigLoader("config.yaml")
        self.imagenes = {}
        self.sonidos = {}
        self.cargar_imagenes()
        self.cargar_sonidos()

    def cargar_imagenes(self):
        for nombre, ruta in self.config.config["imagenes"].items():
            imagen = pygame.image.load(ruta)
            self.imagenes[nombre] = pygame.transform.scale(imagen, (50, 50))

    def cargar_sonidos(self):
        for nombre, ruta in self.config.config["sonidos"].items():
            self.sonidos[nombre] = ruta
    def get_imagen(self, nombre):
        return self.imagenes.get(nombre)

    def get_sonido(self, nombre):
        return self.sonidos.get(nombre)
