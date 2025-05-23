#Registor de mejores puntajes Mariana
import json
import os

ARCHIVO = "mejores_puntajes.json"

def cargar_puntajes():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)