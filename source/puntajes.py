#Registor de mejores puntajes Mariana
import json
from pathlib import Path

ARCHIVO_PUNTAJES = Path(__file__).resolve().parent / "mejores_puntajes.json"
MAX_PUNTAJES = 5

def guardar_puntaje(nombre, puntaje):
    puntajes = []

    # Leer archivo existente
    if ARCHIVO_PUNTAJES.exists():
        with open(ARCHIVO_PUNTAJES, "r") as archivo:
            puntajes = json.load(archivo)

    # Agregar nuevo puntaje
    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    puntajes.sort(key=lambda x: x["puntaje"], reverse=True)
    puntajes = puntajes[:MAX_PUNTAJES]  # Limitar a top 5

    # Guardar de nuevo
    with open(ARCHIVO_PUNTAJES, "w") as archivo:
        json.dump(puntajes, archivo, indent=4)

def mostrar_puntajes():
    if ARCHIVO_PUNTAJES.exists():
        print("\n🏆 Mejores Puntajes:")
        with open(ARCHIVO_PUNTAJES, "r") as archivo:
            puntajes = json.load(archivo)
            for i, entrada in enumerate(puntajes, start=1):
                print(f"{i}. {entrada['nombre']} - {entrada['puntaje']}")
    else:
        print("\nNo hay puntajes guardados todavía.")
