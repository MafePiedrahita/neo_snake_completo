import yaml
from pathlib import Path

class ConfigLoader:
    def __init__(self, ruta_config):
        base_dir = Path(__file__).resolve().parent
        ruta_absoluta = (base_dir / ruta_config).resolve()
        self.config = self.cargar_config(ruta_absoluta)

    def cargar_config(self, ruta):
        if not ruta.exists():
            raise FileNotFoundError(f"Archivo YAML no encontrado: {ruta}")
        with open(ruta, 'r') as f:
            return yaml.safe_load(f)

    def obtener_ruta(self, categoria, nombre):
        try:
            return self.config[categoria][nombre]
        except KeyError:
            raise KeyError(f"No se encontró la ruta para: {categoria} -> {nombre}")
