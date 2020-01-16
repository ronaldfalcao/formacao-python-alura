class Programa:
    pass


class Filme:

    def __init__(self, nome, ano, duracao, likes):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = likes

    """ Métodos de exibição dos atributos"""
    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @ano.setter
    def ano(self, ano):
        self.ano = ano

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @likes.setter
    def likes(self, likes):
        self.__likes = likes

    def dar_likes(self):
        self.likes += 1


class Serie:

    def __init__(self, nome, ano, temporadas, likes):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = likes

    def dar_likes(self):
        self.__likes += 1


# Permite rodar no terminal
if __name__ == '__main__':
    filme = Filme("a morte do caixeiro viajante", 1951, 105, 0)
    filme.dar_likes()
    print(filme.likes)
