# src/cuenta_bancaria.py
class CuentaBancaria:
    """
    Clase que modela una cuenta bancaria simple.
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa la cuenta con un titular y un saldo inicial.
        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Saldo inicial de la cuenta.
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        """
        Agrega dinero a la cuenta.
        :param monto: Cantidad a depositar.
        :raises ValueError: Si el monto es negativo.
        """
        if monto < 0:
            raise ValueError("El monto a depositar no puede ser negativo.")
        self.saldo += monto

    def retirar(self, monto):
        """
        Retira dinero de la cuenta.
        :param monto: Cantidad a retirar.
        :raises ValueError: Si el monto es mayor al saldo disponible.
        """
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        self.saldo -= monto

    def consultar_saldo(self):
        """
        Devuelve el saldo actual de la cuenta.
        :return: Saldo actual.
        """
        return self.saldo
