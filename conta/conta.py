class Conta:
    """Construtor da classe"""
    def __init__(self, numero, titular, saldo,  limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def exibir_estrato(self):
        print(f'O saldo atual é de R$ {self.saldo}')
