#Registor de mejores puntajes Mariana
import json
import os

ARCHIVO = "mejores_puntajes.json"

def cargar_puntajes():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar_puntaje(nombre, puntaje):
    puntajes = cargar_puntajes()
    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:5]
    with open(ARCHIVO, "w") as f:
        json.dump(puntajes, f, indent=4)

def mostrar_puntajes():
    puntajes = cargar_puntajes()
    for idx, p in enumerate(puntajes, 1):
        print(f"{idx}. {p['nombre']} - {p['puntaje']}")