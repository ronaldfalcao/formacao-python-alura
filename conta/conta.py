class Conta:

    """Construtor da classe"""
    def __init__(self, numero, titular, saldo,  limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        print(f'Criando a conta... {self}')

    """Métodos de acesso aos atributos"""
    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    """Métodos para alteração de atributos."""
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    def exibir_extrato(self):
        print(f'O saldo atual é de R$ {self.saldo:.2f}')

    def depositar(self, valor_depositado):
        self.saldo += valor_depositado

    def __pode_sacar(self, valor_a_sacar):
        print(f'{self.saldo + valor_a_sacar}')
        if self.limite >= (self.saldo + valor_a_sacar):
            print(f'Saque autorizado!')
            return True
        else:
            print(f'Saque Não Autorizado. Valor máximo permitido: R$ {self.saldo + self.limite}')
            return False

    def sacar(self, valor_sacado):
        if self.__pode_sacar(valor_sacado):
            self.saldo -= valor_sacado

    def transferir_entre_contas(self, valor_transferencia, conta_destino):
        self.sacar(valor_transferencia)
        conta_destino.depositar(valor_transferencia)
