class Cpf:

    def __init__(self, numero):

        if self.cpf_eh_valido(numero):
            self.numero_documento = numero
            print("CPF criado com sucesso!!!")
        else:
            raise ValueError("Número de CPF inválido! Não possui 11 caracteres.")

    @staticmethod
    def cpf_eh_valido(numero):

        if len(str(numero)) == 11:
            return True
        else:
            return False

    def formatar_cpf(self):

        numero = str(self.numero_documento)
        return f'{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}'

    def __str__(self):
        return self.formatar_cpf()
