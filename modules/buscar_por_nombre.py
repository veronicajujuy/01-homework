import logging


def buscar_por_nombre(lista):
    """
    Busca un nombre en una lista de nombres y devuelve la posición del nombre en la lista.
    Si el nombre no se encuentra, devuelve None.

    :param lista: Lista de nombres
    :return: Posición del nombre en la lista o None si no se encuentra
    """
    if not lista:
        print("La lista está vacía.")
        return None

    nombre = input("Ingrese el nombre a buscar: ").lower().strip()

    try:
        assert len(nombre) > 0, "El nombre no puede estar vacío."

        for item in lista:
            if item["nombre"].lower() == nombre:
                return item

    except AssertionError as e:
        logging.error(f"Error: {e}")
        return None

    logging.warn(f"El nombre '{nombre}' no se encontró en la lista.")
    return None
