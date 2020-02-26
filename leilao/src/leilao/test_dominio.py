from unittest import TestCase
from leilao.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_avaliar_quando_dois_lances(self):
        """
        Teste para avaliar o cenário com dois lances.
        """

        usuario_a = Usuario("A")
        usuario_b = Usuario("B")

        lance_usuario_a = Lance(usuario_b, 100.0)
        lance_usuario_b = Lance(usuario_a, 110.0)

        leilao = Leilao("Leilão de Exemplo")

        leilao.lances.append(lance_usuario_a)
        leilao.lances.append(lance_usuario_b)

        avaliador = Avaliador()
        avaliador.avaliar(leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(110.00, avaliador.maior_lance)

    def test_avaliar_quando_ordem_invertida(self):
        """
        Teste para avaliar da mesma forma que o teste acima (test_avaliar), mas invertendo
        a ordem de inserção dos lances com o critério de maior e menor valores invertidos.
        """

        usuario_a = Usuario("A")
        usuario_b = Usuario("B")

        lance_usuario_a = Lance(usuario_b, 100.0)
        lance_usuario_b = Lance(usuario_a, 110.0)

        leilao = Leilao("Leilão de Exemplo")

        leilao.lances.append(lance_usuario_b)  # Inverteu essas linhas
        leilao.lances.append(lance_usuario_a)

        avaliador = Avaliador()
        avaliador.avaliar(leilao)

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

        usuario_a = Usuario("A")
        usuario_b = Usuario("B")
        usuario_c = Usuario("C")

        lance_usuario_a = Lance(usuario_a, 100.0)
        lance_usuario_b = Lance(usuario_b, 110.0)
        lance_usuario_c = Lance(usuario_c, 200.0)

        leilao = Leilao("Leilão de Exemplo")

        leilao.lances.append(lance_usuario_a)  # Inverteu essas linhas
        leilao.lances.append(lance_usuario_b)
        leilao.lances.append(lance_usuario_c)

        avaliador = Avaliador()
        avaliador.avaliar(leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(200.00, avaliador.maior_lance)