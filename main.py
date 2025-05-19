# HOMEWORK
from modules.listar_usuarios import listar_usuarios
from modules.registrar_usuario import registrar_usuario
from modules.buscar_por_nombre import buscar_por_nombre
from modules.eliminar_usuario import eliminar_usuario
from modules.guardar_archivo import guardar_archivo, cargar_archivo

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

lista_usuarios = []

while True:
    try:
        print("Bienvenido al sistema de gestión de usuarios.")
        print("1. Registrar usuario")
        print("2. Listar usuarios registrados")
        print("3. Buscar usuario por nombre")
        print("4. Eliminar usuario")
        print("5. Guardar y cargar lista de usuarios en archivos externos")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_usuario(lista_usuarios)
        elif opcion == 2:
            listar_usuarios(lista_usuarios)
        elif opcion == 3:
            usuario = buscar_por_nombre(lista_usuarios)
            if usuario is not None:
                print(
                    f"Usuario encontrado: {usuario['nombre']}, Email: {usuario['email']}"
                )
        elif opcion == 4:
            eliminar_usuario(lista_usuarios)
        elif opcion == 5:
            cargar_guardar = (
                input(
                    "¿Desea cargar o guardar la lista de usuarios? 'c' (cargar)/'g' guardar): "
                )
                .strip()
                .lower()
            )
            if cargar_guardar == "c":
                lista_usuarios = cargar_archivo()
                print("Lista de usuarios cargada con éxito.")
            elif cargar_guardar == "g":
                guardar_archivo(lista_usuarios)
                print("Lista de usuarios guardada con éxito.")
            else:
                print("Opción no válida. Debe ingresar 'c' (cargar) o 'g' (guardar).")
        else:
            logging.info("Opción no válida. Intente nuevamente.")
    except ValueError:
        logging.error("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    if opcion != 6:
        logging.info("presione cualquier tecla para continuar")
        input()
    else:
        print("Saliendo del sistema. ¡Hasta luego!")
        break
