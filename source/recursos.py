import pygame
from pathlib import Path
from source.config_loader import ConfigLoader

class Recursos:
    def __init__(self):
        # Ruta absoluta al archivo config.yaml (subiendo desde source/)
        ruta_config = Path(__file__).resolve().parent.parent / "config.yaml"
        self.config = ConfigLoader(ruta_config)
        self.imagenes = {}
        self.sonidos = {}
        self.cargar_imagenes()
        self.cargar_sonidos()

    def cargar_imagenes(self):
        for nombre, ruta in self.config.config["imagenes"].items():
            try:
                imagen = pygame.image.load(ruta)
                imagen = pygame.transform.scale(imagen, (50, 50))
                self.imagenes[nombre] = imagen
            except Exception as e:
                print(f"[Error] No se pudo cargar la imagen '{nombre}' desde '{ruta}': {e}")

    def cargar_sonidos(self):
        for nombre, ruta in self.config.config["sonidos"].items():
            self.sonidos[nombre] = ruta  # puedes usar pygame.mixer.music.load si lo deseas

    def get_imagen(self, nombre):
        imagen = self.imagenes.get(nombre)
        if imagen is None:
            print(f"[Advertencia] Imagen '{nombre}' no encontrada en recursos.")
        return imagen

    def get_sonido(self, nombre):
        sonido = self.sonidos.get(nombre)
        if sonido is None:
            print(f"[Advertencia] Sonido '{nombre}' no encontrado en recursos.")
        return sonido

