from leilao.src.leilao.dominio import Usuario, Leilao


def test_descontar_valor_lance_carteira_usuario():

    usuario_a = Usuario("A", 100)
    leilao = Leilao("Exemplo Leilão")
    usuario_a.propor_lance(leilao, 50)

    assert usuario_a.carteira == 50


def test_permite_lance_menor_total_carteira_usuario():

    usuario_a = Usuario("A", 100)
    leilao = Leilao("Exemplo Leilão")
    usuario_a.propor_lance(leilao, 1)

    assert usuario_a.carteira == 99.0


def test_permite_lance_valor_igual_valor_carteira_usuario():

    usuario_a = Usuario("A", 100)
    leilao = Leilao("Exemplo Leilão")
    usuario_a.propor_lance(leilao, 100)

    assert usuario_a.carteira == 0


def test_nao_permite_lance_acima_valor_carteira_usuario():

    usuario_a = Usuario("A", 100)
    leilao = Leilao("Exemplo Leilão")
    usuario_a.propor_lance(leilao, 200)

    assert usuario_a.carteira == 100
