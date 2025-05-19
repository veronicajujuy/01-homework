# 🧑‍💻 Sistema de Gestión de Usuarios en Python

Este proyecto es una aplicación de consola interactiva para gestionar usuarios, desarrollada en Python. Permite registrar, listar, buscar, eliminar y guardar usuarios en un archivo `.json`, utilizando un diseño modular.

---

## 🚀 Funcionalidades

- Registrar nuevos usuarios.
- Listar todos los usuarios registrados.
- Buscar usuarios por nombre.
- Eliminar usuarios existentes.
- Guardar y cargar la lista de usuarios en un archivo externo JSON.
- Uso de variables de entorno (.env) para definir la ruta del archivo de almacenamiento.

---

## 📁 Estructura del Proyecto

```css
gestor_usuarios/
├── main.py
├── .env
├── requirements.txt
├── usuarios.json (se crea al guardar)
└── modules/
    ├── listar_usuarios.py
    ├── registrar_usuario.py
    ├── buscar_por_nombre.py
    ├── eliminar_usuario.py
    └── guardar_archivo.py
```

## 🧪 Requisitos

- Python 3.8 o superior
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 🔧 Configuración del entorno
Crear un archivo .env en la raíz del proyecto con la siguiente variable:

```bash
RUTA_ARHIVO=usuarios.json
```
Podés cambiar el nombre o la ruta del archivo (por ejemplo, data/usuarios.json), y el sistema lo creará automáticamente si no existe.

## 📌 Uso
Ejecutá el programa principal:

```bash
python main.py
```
Luego seguí el menú interactivo:

1. Registrar usuario
2. Listar usuarios registrados
3. Buscar usuario por nombre
4. Eliminar usuario
5. Guardar o cargar usuarios desde archivo
6. Salir

## 🛠️ Ejemplo de usuario

Un usuario es representado como un diccionario:

```json
{
  "id": 1,
  "nombre": "Ana",
  "email": "ana@example.com"
}
```

## ✅ Buenas prácticas aplicadas
Código modular: cada función está en su propio archivo.

Manejo de errores con excepciones.

Separación de configuración con .env.

Compatible con múltiples entornos y fácilmente extensible.

📝 Licencia
Este proyecto es parte de una homework de práctica educativa. Libre para usar y modificar con fines de aprendizaje. 😊