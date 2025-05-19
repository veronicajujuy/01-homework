def listar_usuarios(lista_usuarios):
    """
    Esta función lista todos los usuarios registrados en el sistema.
    """
    print("Lista de usuarios registrados: ---------")

    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in lista_usuarios:
        print(f"Nombre: {usuario['nombre']}, Email: {usuario['email']}")
