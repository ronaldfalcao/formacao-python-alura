from unittest import TestCase
from leilao.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_avaliar(self):

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

    def test_avaliar_ordem_invertida(self):

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