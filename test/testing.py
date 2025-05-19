import unittest
from unittest.mock import patch

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # Agregar la ruta al directorio padre

from modules.registrar_usuario import registrar_usuario


class TestRegistrarUsuario(unittest.TestCase):
    @patch("builtins.input", side_effect=["Juan", "juan@example.com", "password123"])
    def test_registrar_usuario(self, mock_input):
        lista_usuarios = []
        resultado = registrar_usuario(lista_usuarios)

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["nombre"], "Juan")
        self.assertEqual(resultado[0]["email"], "juan@example.com")
        self.assertEqual(resultado[0]["password"], "password123")


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
