class Filme:

    def __init__(self, nome, ano, duracao, likes):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = likes

    def dar_likes(self):
        self.likes += 1


class Serie:

    def __init__(self, nome, ano, temporadas, likes):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = likes

    def dar_likes(self):
        self.likes += 1


filme = Filme("a morte do caixeiro viajante", 1951, 105, 0)
