"""
Classe de exemplo para o curso Testes Automatizados: TDD com Python
O arquivo inicial faz parte do curso fornecido pela Alura.
"""

import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

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

        if not self.lances or self.__lances[-1].usuario != lance.usuario:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("Não é possível dar dois lances seguidos.")
