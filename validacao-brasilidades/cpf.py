from validate_docbr import CPF

class Cpf:

    def __init__(self, numero):

        if self.cpf_eh_valido(numero):
            self.numero_documento = numero
            print("CPF criado com sucesso!!!")
        else:
            raise ValueError("Número de CPF inválido! Não possui 11 caracteres.")

    @staticmethod
    def cpf_eh_valido(numero):

        validador = CPF()

        if validador.validate(str(numero)):
            return True
        else:
            return False

    def formatar_cpf(self):

        mascara = CPF()
        return mascara.mask(str(self.numero_documento))

    def __str__(self):
        return self.formatar_cpf()
