from cpf import Cpf
from cnpj import Cnpj


class CpfCnpj:

    @staticmethod
    def criar_novo_documento(documento, tipo_documento):

        if tipo_documento == 'cpf':
            return Cpf(documento)
        elif tipo_documento == 'cnpj':
            return Cnpj(documento)
        else:
            raise ValueError("Número de Documento Inválido, utilize 11 (CFP) ou 14 (CNPJ) caracteres.")


