from validate_docbr import CNPJ


class Cnpj:

    def __init__(self, numero):

        if self.cnpj_eh_valido(numero):
            self.numero_documento = numero
            print("CNPJ criado com sucesso!!!")
        else:
            raise ValueError("Número de CNPJ inválido! Não possui 14 caracteres.")

    @staticmethod
    def cnpj_eh_valido(numero):

        validador = CNPJ()

        if validador.validate(str(numero)):
            return True
        else:
            return False

    def formatar_cnpj(self):

        mascara = CNPJ()
        return mascara.mask(str(self.numero_documento))

    def __str__(self):
        return self.formatar_cnpj()
