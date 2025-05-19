import json
from decouple import config

RUTA_ARCHIVO = config("RUTA_ARCHIVO", default="usuarios.json")


def guardar_archivo(lista):
    """
    Guarda la lista de usuarios en un archivo JSON.

    :param lista: Lista de usuarios
    """
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
    print("Lista de usuarios guardada en 'usuarios.json' con éxito.")


def cargar_archivo():
    """
    Carga la lista de usuarios desde un archivo JSON.

    :param lista: Lista de usuarios
    :return: Lista de usuarios cargada
    """
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lista = json.load(archivo)
        print(f"Lista de usuarios cargada desde {RUTA_ARCHIVO} con éxito.")
    except FileNotFoundError:
        print("El archivo 'usuarios.json' no se encontró.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []
    return lista
