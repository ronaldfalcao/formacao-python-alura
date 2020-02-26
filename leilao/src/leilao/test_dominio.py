from unittest import TestCase
from leilao.src.leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        """
        Método para isolar a criação de cenários de teste.
        """
        self.usuario_a = Usuario("A")
        self.usuario_b = Usuario("B")

        self.lance_usuario_a = Lance(self.usuario_a, 100.0)
        self.lance_usuario_b = Lance(self.usuario_b, 110.0)

        self.leilao = Leilao("Leilão de Exemplo")

    def test_avaliar_quando_dois_lances(self):
        """
        Teste para avaliar o cenário com dois lances.
        """

        self.leilao.propor(self.lance_usuario_a)
        self.leilao.propor(self.lance_usuario_b)

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(110.00, self.leilao.maior_lance)

    def test_avaliar_quando_ordem_invertida(self):
        """
        Teste para avaliar da mesma forma que o teste acima (test_avaliar), mas invertendo
        a ordem de inserção dos lances com o critério de maior e menor valores invertidos.
        """

        self.leilao.propor(self.lance_usuario_b)  # Inverteu essas linhas
        self.leilao.propor(self.lance_usuario_a)

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(110.00, self.leilao.maior_lance)

    def test_avaliar_quando_houver_um_lance(self):
        """
        Teste para verificar as regras se houver apenas um lance.
        """

        self.usuario_a = Usuario("A")
        self.lance_usuario_a = Lance(self.usuario_a, 100.0)
        leilao = Leilao("Leilão de Exemplo")

        self.leilao.propor(self.lance_usuario_a)  # Inverteu essas linhas

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(100.00, self.leilao.maior_lance)

    def test_avaliar_quando_tres_lances(self):
        """
        Teste para avaliar da mesma forma que o teste acima (test_avaliar), mas invertendo
        a ordem de inserção dos lances com o critério de maior e menor valores invertidos.
        """

        self.usuario_c = Usuario("C")

        self.lance_usuario_c = Lance(self.usuario_c, 200.0)

        self.leilao.propor(self.lance_usuario_a)  # Inverteu essas linhas
        self.leilao.propor(self.lance_usuario_b)
        self.leilao.propor(self.lance_usuario_c)

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(200.00, self.leilao.maior_lance)
