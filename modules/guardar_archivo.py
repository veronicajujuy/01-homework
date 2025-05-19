import json


def guardar_archivo(lista):
    """
    Guarda la lista de usuarios en un archivo JSON.

    :param lista: Lista de usuarios
    """
    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
    print("Lista de usuarios guardada en 'usuarios.json' con éxito.")


def cargar_archivo():
    """
    Carga la lista de usuarios desde un archivo JSON.

    :param lista: Lista de usuarios
    :return: Lista de usuarios cargada
    """
    try:
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            lista = json.load(archivo)
        print("Lista de usuarios cargada desde 'usuarios.json' con éxito.")
    except FileNotFoundError:
        print("El archivo 'usuarios.json' no se encontró.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    return lista
