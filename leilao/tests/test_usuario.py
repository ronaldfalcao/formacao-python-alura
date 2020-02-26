from leilao.src.leilao.dominio import Usuario, Leilao
import pytest


@pytest.fixture
def criar_usuario():
    return Usuario("A", 100)


def test_descontar_valor_lance_carteira_usuario(criar_usuario):

    leilao = Leilao("Exemplo Leilão")
    criar_usuario.propor_lance(leilao, 50)

    assert criar_usuario.carteira == 50


def test_permite_lance_menor_total_carteira_usuario(criar_usuario):

    leilao = Leilao("Exemplo Leilão")
    criar_usuario.propor_lance(leilao, 1)

    assert criar_usuario.carteira == 99.0


def test_permite_lance_valor_igual_valor_carteira_usuario(criar_usuario):

    leilao = Leilao("Exemplo Leilão")
    criar_usuario.propor_lance(leilao, 100)

    assert criar_usuario.carteira == 0


def test_nao_permite_lance_acima_valor_carteira_usuario(criar_usuario):

    with pytest.raises(ValueError):
        leilao = Leilao("Exemplo Leilão")
        criar_usuario.propor_lance(leilao, 200)

