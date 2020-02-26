from unittest import TestCase
from leilao.src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        """
        Método para isolar a criação de cenários de teste.
        """
        self.usuario_a = Usuario("A", 500.00)
        self.usuario_b = Usuario("B", 500.00)

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
        Teste para avaliar se o lance proposto é maior do que o último lance dado.
        """

        with self.assertRaises(ValueError):
            self.leilao.propor(self.lance_usuario_b)  # Inverteu essas linhas
            self.leilao.propor(self.lance_usuario_a)

    def test_avaliar_quando_houver_um_lance(self):
        """
        Teste para verificar as regras se houver apenas um lance.
        """

        self.usuario_a = Usuario("A", 500.00)
        self.lance_usuario_a = Lance(self.usuario_a, 100.0)

        self.leilao.propor(self.lance_usuario_a)  # Inverteu essas linhas

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(100.00, self.leilao.maior_lance)

    def test_avaliar_quando_tres_lances(self):
        """
        Teste para avaliar da mesma forma que o teste acima (test_avaliar), mas invertendo
        a ordem de inserção dos lances com o critério de maior e menor valores invertidos.
        """

        self.usuario_c = Usuario("C", 500.00)

        self.lance_usuario_c = Lance(self.usuario_c, 200.0)

        self.leilao.propor(self.lance_usuario_a)  # Inverteu essas linhas
        self.leilao.propor(self.lance_usuario_b)
        self.leilao.propor(self.lance_usuario_c)

        self.assertEqual(100.00, self.leilao.menor_lance)
        self.assertEqual(200.00, self.leilao.maior_lance)

    def test_propor_lance_quando_nao_ha_lances(self):

        self.leilao.propor(self.lance_usuario_a)
        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances)

    def test_propor_lance_quando_ultimo_usuario_for_diferente(self):

        self.usuario_c = Usuario("C", 500.00)
        self.lance_usuario_c = Lance(self.usuario_c, 200.0)

        self.leilao.propor(self.lance_usuario_a)
        self.leilao.propor(self.lance_usuario_c)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)

    def test_nao_permitir_dois_lances_seguidos_mesmo_usuario(self):

        self.usuario_c = Usuario("C", 500.00)

        with self.assertRaises(ValueError):
            self.lance_usuario_c = Lance(self.usuario_c, 200.0)
            self.leilao.propor(self.lance_usuario_c)

            self.lance_usuario_c = Lance(self.usuario_c, 250.0)
            self.leilao.propor(self.lance_usuario_c)
