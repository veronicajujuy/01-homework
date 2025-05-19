import logging


def eliminar_usuario(lista):
    """
    Elimina un usuario de la lista de usuarios.

    :param lista: Lista de usuarios
    :return: Lista actualizada de usuarios
    """
    if not lista:
        print("La lista está vacía.")
        return lista

    nombre = input("Ingrese el nombre del usuario a eliminar: ").lower().strip()

    try:
        assert len(nombre) > 0, "El nombre no puede estar vacío."

        for usuario in lista:
            if usuario["nombre"].lower() == nombre:
                lista.remove(usuario)
                print(f"Usuario '{nombre}' eliminado con éxito.")
                return lista

    except AssertionError as e:
        logging.error(f"Error: {e}")
        return lista

    logging.warning(f"El usuario '{nombre}' no se encontró en la lista.")
    return lista
