import re


class Telefones:

    _padrao_br = '([0-9]{2,3})?([0-9]{2})([0-9]{3,4})([0-9]{4})'  # Constante para o padrão

    def __init__(self, numero_telefone):

        if self.valida_telefone(numero_telefone):
            self.numero_telefone = numero_telefone
        else:
            raise ValueError("O número de telefone é inválido para o padrão BR.")

    def valida_telefone(self, numero_telefone):

        if self.retorna_padrao_telefone(numero_telefone):
            return True
        else:
            return False

    def retorna_padrao_telefone(self, numero_telefone):
        return re.findall(self._padrao_br, numero_telefone)

    def formata_telefone(self):

        numero_formatado = re.search(self._padrao_br, self.numero_telefone)

        return f'+{numero_formatado.group(1)} ' \
               f'({numero_formatado.group(2)})' \
               f'{numero_formatado.group(3)}-{numero_formatado.group(4)}'

    def __str__(self):
        return self.formata_telefone()
