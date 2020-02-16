from cpf import Cpf
from cnpj import Cnpj


class Documento:

    @staticmethod
    def criar_novo_documento(documento):
        """ Criação de documentos
            Tipos Permitidos: cpf e cnpj.
        """

        if len(documento) == 11:
            return Cpf(documento)

        if len(documento) == 14:
            return Cnpj(documento)

        raise ValueError("Esse tipo de documento não está cadastrado no sistema.")
