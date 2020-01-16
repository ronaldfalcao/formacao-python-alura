from abc import ABCMeta, abstractmethod


class Retangulo:

    @abstractmethod
    def get_lado_maior(self, lado_maior):
        pass


class Quadrado(Retangulo):  # Apresenta erro pq não foram implementados os métodos
    # estáticos da superclasse

    @staticmethod
    def area(lado):
        return lado * lado


# Permite rodar no terminal
if __name__ == '__main__':
    quadrado = Quadrado()
    print(quadrado.area(10))
