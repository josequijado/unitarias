# subtests_multiples.py

import unittest
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

class TestOperaciones(unittest.TestCase):
    def test_operaciones(self):
        """
        Usa subtests para probar diferentes funciones.
        """
        casos = [
            (suma, 1, 2, 3),  # función, a, b, resultado esperado
            (resta, 5, 3, 2),
            (suma, -1, -1, -2),
            (resta, 10, 5, 5),
        ]

        for funcion, a, b, esperado in casos:
            with self.subTest(funcion=funcion.__name__, a=a, b=b, esperado=esperado):
                resultado = funcion(a, b)
                self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
