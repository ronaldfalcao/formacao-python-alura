class Conta:

    """Construtor da classe"""
    def __init__(self, numero, titular, saldo,  limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        print(f'Criando a conta... {self}')

    def exibir_extrato(self):
        print(f'O saldo atual é de R$ {self.__saldo:.2f}')

    def depositar(self, valor_depositado):
        self.__saldo += valor_depositado

    def sacar(self, valor_sacado):
        self.__saldo -= valor_sacado

    def transferir_entre_contas(self, valor_transferencia, conta_destino):
        self.sacar(valor_transferencia)
        conta_destino.depositar(valor_transferencia)
