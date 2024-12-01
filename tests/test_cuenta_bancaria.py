# tests/test_cuenta_bncaria.py

import unittest
from src.cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase CuentaBancaria.
    """

    def setUp(self):
        """
        Configura una cuenta bancaria inicial para las pruebas.
        """
        self.cuenta = CuentaBancaria("Juan Pérez", saldo_inicial=100)

    def test_retiro_excesivo_lanza_excepcion(self):
        """
        Verifica que se lance una excepción al intentar retirar más dinero del saldo disponible.
        """
        with self.assertRaises(ValueError) as contexto:
            self.cuenta.retirar(200)  # Intento de retiro mayor al saldo disponible

        # Verificamos el mensaje exacto de la excepción
        self.assertEqual(str(contexto.exception), "Fondos insuficientes para realizar el retiro.")

    def test_deposito_negativo_lanza_excepcion(self):
        """
        Verifica que se lance una excepción al intentar depositar un monto negativo.
        """
        with self.assertRaises(ValueError) as contexto:
            self.cuenta.depositar(-50)  # Intento de depositar un valor negativo

        # Verificamos el mensaje exacto de la excepción
        self.assertEqual(str(contexto.exception), "El monto a depositar no puede ser negativo.")

    def test_retiro_valido_no_lanza_excepcion(self):
        """
        Verifica que un retiro válido no lance ninguna excepción y actualice correctamente el saldo.
        """
        try:
            self.cuenta.retirar(50)  # Retiro válido
        except Exception as e:
            self.fail(f"No se esperaba ninguna excepción, pero se lanzó: {e}")

        # Verificamos que el saldo se haya actualizado correctamente
        self.assertEqual(self.cuenta.consultar_saldo(), 50)

    def test_deposito_valido_no_lanza_excepcion(self):
        """
        Verifica que un depósito válido no lance ninguna excepción y actualice correctamente el saldo.
        """
        try:
            self.cuenta.depositar(200)  # Depósito válido
        except Exception as e:
            self.fail(f"No se esperaba ninguna excepción, pero se lanzó: {e}")

        # Verificamos que el saldo se haya actualizado correctamente
        self.assertEqual(self.cuenta.consultar_saldo(), 300)


if __name__ == '__main__':
    unittest.main()
