import re


class Telefones:

    def __init__(self, numero_telefone):

        if self.valida_telefone(numero_telefone):
            self.numero_telefone = numero_telefone
        else:
            raise ValueError("O número de telefone é inválido para o padrão BR.")

    @staticmethod
    def valida_telefone(numero_telefone):

        padrao_br = '[0-9]{2,3}[0-9]{2}[0-9]{3,4}[0-9]{4}'

        resposta = re.findall(padrao_br, numero_telefone)

        if resposta:
            return True
        else:
            return False

    def __str__(self):
        return self.numero_telefone
