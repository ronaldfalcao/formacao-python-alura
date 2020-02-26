from unittest import TestCase
from leilao.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


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

        avaliador = Avaliador()
        avaliador.avaliar(self.leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(110.00, avaliador.maior_lance)

    def test_avaliar_quando_ordem_invertida(self):
        """
        Teste para avaliar da mesma forma que o teste acima (test_avaliar), mas invertendo
        a ordem de inserção dos lances com o critério de maior e menor valores invertidos.
        """

        leilao = Leilao("Leilão de Exemplo")

        self.leilao.lances.append(self.lance_usuario_b)  # Inverteu essas linhas
        self.leilao.lances.append(self.lance_usuario_a)

        avaliador = Avaliador()
        avaliador.avaliar(self.leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(110.00, avaliador.maior_lance)

    def test_avaliar_quando_houver_um_lance(self):
        """
        Teste para verificar as regras se houver apenas um lance.
        """

        usuario_a = Usuario("A")

        lance_usuario_a = Lance(usuario_a, 100.0)

        leilao = Leilao("Leilão de Exemplo")

        leilao.lances.append(lance_usuario_a)  # Inverteu essas linhas

        avaliador = Avaliador()
        avaliador.avaliar(leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(100.00, avaliador.maior_lance)

    def test_avaliar_quando_tres_lances(self):
        """
        Teste para avaliar da mesma forma que o teste acima (test_avaliar), mas invertendo
        a ordem de inserção dos lances com o critério de maior e menor valores invertidos.
        """

        usuario_c = Usuario("C")

        lance_usuario_c = Lance(usuario_c, 200.0)

        self.leilao.lances.append(self.lance_usuario_a)  # Inverteu essas linhas
        self.leilao.lances.append(self.lance_usuario_b)
        self.leilao.lances.append(lance_usuario_c)

        avaliador = Avaliador()
        avaliador.avaliar(self.leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(200.00, avaliador.maior_lance)