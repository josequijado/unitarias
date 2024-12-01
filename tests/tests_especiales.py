# tests/test_especiales.py
import unittest  # Importamos el framework para pruebas unitarias
from src.ejemplo_operaciones import suma  # Importamos la función a probar

class TestSuma(unittest.TestCase):
    """
    Clase que agrupa las pruebas para la función `suma`.
    """

    def setUp(self):
        """
        Método que se ejecuta automáticamente antes de cada prueba.
        Ideal para inicializar datos, configurar dependencias o crear recursos temporales.
        """
        print("Inicio de test")  # Este mensaje aparecerá antes de cada prueba
        self.num_a = 0  # Inicializamos variables comunes para las pruebas
        self.num_b = 0

    def tearDown(self):
        """
        Método que se ejecuta automáticamente después de cada prueba.
        Útil para limpiar recursos, resetear estados o liberar memoria.
        """
        print("Finalización de test")  # Este mensaje aparecerá después de cada prueba
        del self.num_a
        del self.num_b

    def test_suma_positivos(self):
        """
        Prueba la suma de dos números positivos.
        """
        self.num_a = 2
        self.num_b = 3
        resultado = suma(self.num_a, self.num_b)
        self.assertEqual(resultado, 5)

    def test_suma_negativos(self):
        """
        Prueba la suma de dos números negativos.
        """
        self.num_a = -1
        self.num_b = -1
        resultado = suma(self.num_a, self.num_b)
        self.assertEqual(resultado, -2)

    def test_suma_cero(self):
        """
        Prueba la suma de ceros.
        """
        self.num_a = 0
        self.num_b = 0
        resultado = suma(self.num_a, self.num_b)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':
    unittest.main()
