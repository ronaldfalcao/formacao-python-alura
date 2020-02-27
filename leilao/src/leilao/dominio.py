"""
Classe de exemplo para o curso Testes Automatizados: TDD com Python
O arquivo inicial faz parte do curso fornecido pela Alura.
"""
from excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome

    def propor_lance(self, leilao, valor):

        if not self.valor_eh_valido(valor):
            raise LanceInvalido(f'Valor maior do que permitido. Diferença {self.__carteira - valor}')
        else:
            lance = Lance(self, valor)
            leilao.propor(lance)
            self.__carteira -= valor

    def valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0  # Não é mais necessário definir esses valores como maior e menor.
        self.menor_lance = 0.0

    @property
    def lances(self):
        """
        Método para criar os lances, evitando o uso do append() de forma direta. Assim, sempre
        utilizar o método propor().
        """
        return self.__lances[:]  # Criando uma cópia rasa da lista.

    def propor(self, lance: Lance):
        """
        Método para encapsulamento dos lances feitos na classe Leilao(). Dessa forma podemos mudar
        a forma de fazermos os lances, alterando por exemplo o tipo do dado (numpy array, grupos,
        dicionários, etc.).

        "Tell, don't ask!!!!!!"

        """

        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise LanceInvalido("Erro ao propor lance.")

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _maior_que_lance_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_eh_valido(self, lance):
        return not self.lances or \
               (self._usuarios_diferentes(lance)) and \
               (self._maior_que_lance_anterior(lance))
