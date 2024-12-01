# tests/test_operaciones
import unittest  # Importamos el framework para pruebas unitarias
from src.ejemplo_operaciones import suma  # Importamos la función a probar

class TestSuma(unittest.TestCase):
    """
    Clase que agrupa las pruebas para la función `suma`.
    """

    def test_suma_positivos(self):
        """
        Prueba la suma de dos números positivos.
        """
        resultado = suma(2, 3)
        self.assertEqual(resultado, 5)

    def test_suma_negativos(self):
        """
        Prueba la suma de dos números negativos.
        """
        resultado = suma(-1, -1)
        self.assertEqual(resultado, -2)

    def test_suma_cero(self):
        """
        Prueba la suma de ceros.
        """
        resultado = suma(0, 0)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
