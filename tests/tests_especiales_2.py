import unittest  # Importamos el framework para pruebas unitarias
from src.ejemplo_operaciones import suma  # Importamos la función a probar

class TestSuma(unittest.TestCase):
    """
    Clase que agrupa las pruebas para la función `suma`.
    """

    def setUp(self):
        """
        Configuración previa al test.
        """
        print(f"\n[Preparando entorno] Test en ejecución: {self._testMethodName}")

    def tearDown(self):
        """
        Limpieza posterior al test.
        Determina si el test pasó o falló utilizando `self._outcome`.
        """
        # Accedemos al resultado del test actual
        outcome = getattr(self, '_outcome', None)
        if outcome:
            # Buscamos errores en el test actual
            test_result = outcome.result
            if test_result:
                errors = test_result.errors
                failures = test_result.failures

                # Determinamos si este test específico tuvo errores o fallos
                test_name = self._testMethodName
                current_test_error = any(test == self for test, _ in errors)
                current_test_failure = any(test == self for test, _ in failures)

                if current_test_error or current_test_failure:
                    print(f"[Limpieza del entorno] Test '{test_name}' falló.")
                else:
                    print(f"[Limpieza del entorno] Test '{test_name}' finalizado exitosamente.")
        else:
            print("[Limpieza del entorno] No se pudo determinar el resultado del test.")

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
        self.assertEqual(resultado, 0)  # Forzamos fallo deliberado


if __name__ == '__main__':
    unittest.main()
