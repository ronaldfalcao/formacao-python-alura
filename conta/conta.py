class Conta:

    """Construtor da classe"""
    def __init__(self, numero, titular, saldo,  limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        print(f'Criando a conta... {self}')

    def exibir_extrato(self):
        print(f'O saldo atual é de R$ {self.saldo:.2f}')

    def depositar(self, valor_depositado):
        self.saldo += valor_depositado

    def sacar(self, valor_sacado):
        self.saldo -= valor_sacado
