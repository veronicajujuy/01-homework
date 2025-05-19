def registrar_usuario(lista_usuarios):
    
    """
    Esta función registra un nuevo usuario en el sistema.
    """
    print("Registro de nuevo usuario")
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")

    print(f"Usuario {nombre} {email} registrado con éxito.")

    lista_usuarios.append(
        {
            "nombre": nombre,
            "email": email,
            "password": password,
        }
    )

    return lista_usuarios
