#subtest_simple.py
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_varios_casos(self):
        """
        Usa subtests para verificar múltiples casos de suma.
        """
        casos = [
            (1, 2, 3),  # a, b, resultado esperado
            (2, 2, 4),
            (0, 0, 0),
            (-1, -1, -2),
            (100, 200, 500)
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b, esperado=esperado):
                resultado = suma(a, b)
                self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
