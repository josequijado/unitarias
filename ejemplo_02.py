import unittest  # Importamos el módulo unittest, parte de la biblioteca estándar de Python.

# Función que queremos probar.
def suma(a, b):
    """
    Esta función toma dos argumentos (a y b) y devuelve su suma.
    """
    return a + b

# Clase de prueba que agrupa las pruebas para la función `suma`.
class TestSuma(unittest.TestCase):
    """
    Esta clase contiene pruebas unitarias para la función `suma`.
    Hereda de `unittest.TestCase`, que proporciona las herramientas necesarias para las pruebas.
    Las clases que se crean para ejecutar tests deben nombrarse siempre iniciando el nombre
    con el prefijo Test (con la primera T mayúscula), como vemos en TestSuma.
    """

    def setUp(self):
        """
        Método opcional que se ejecuta antes de cada prueba.
        Se usa para preparar el entorno o inicializar valores necesarios.
        Aquí no hacemos nada porque no necesitamos configuración previa.
        """
        pass

    def tearDown(self):
        """
        Método opcional que se ejecuta después de cada prueba.
        Se usa para limpiar recursos o restablecer configuraciones.
        Aquí tampoco hacemos nada porque no hay recursos que limpiar.
        """
        pass

    # Primera prueba: Verifica que la suma de dos números positivos sea correcta.
    """
    Los métodos de prueba deben nombrarse siempre empezando con el prefjo test_ como en 
    test_suma_positivos, test_suma_negativos y test_suma_cero.
    """
    def test_suma_positivos(self):
        """
        Prueba que la función `suma` devuelve el resultado correcto
        cuando ambos números son positivos.
        """
        resultado = suma(2, 3)  # Llamamos a la función con los valores 2 y 3.
        self.assertEqual(resultado, 5)  # Verificamos que el resultado sea igual a 5.

    # Segunda prueba: Verifica que la suma de dos números negativos sea correcta.
    def test_suma_negativos(self):
        """
        Prueba que la función `suma` devuelve el resultado correcto
        cuando ambos números son negativos.
        """
        resultado = suma(-1, -1)  # Llamamos a la función con los valores -1 y -1.
        self.assertEqual(resultado, -2)  # Verificamos que el resultado sea igual a -2.

    # Tercera prueba: Verifica que la suma de dos ceros sea cero.
    def test_suma_cero(self):
        """
        Prueba que la función `suma` devuelve el resultado correcto
        cuando ambos números son cero.
        """
        resultado = suma(0, 0)  # Llamamos a la función con los valores 0 y 0.
        self.assertEqual(resultado, 0)  # Verificamos que el resultado sea igual a 0.

# Este bloque asegura que las pruebas se ejecuten solo si este archivo
# se ejecuta directamente, y no si es importado como un módulo.
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)  # Nivel de detalle
    unittest.main(testRunner=runner)
