import requests


class BuscaEndereco:

    def __init__(self, cep):

        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError("O CEP informado não está correto")

    def __str__(self):
        return self.formata_cep()

    @staticmethod
    def validar_cep(cep):

        if len(str(cep)) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def retorna_url_via_cep(self):
        return f'https://viacep.com.br/ws/{self.cep}/json/'

    def acessa_via_cep(self):

        r = requests.get(self.retorna_url_via_cep())

        dados = r.json()

        return f'{dados["cep"]} - {dados["localidade"]}/{dados["uf"]}'

