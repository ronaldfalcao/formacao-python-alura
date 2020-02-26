from leilao.src.leilao.dominio import Lance, Leilao, Usuario
from leilao.src.leilao.dominio import Avaliador

usuario_a = Usuario("A")
usuario_b = Usuario("B")

lance_usuario_a = Lance(usuario_a, 100.0)
lance_usuario_b = Lance(usuario_b, 90.0)

leilao = Leilao("Leilão de Exemplo")

leilao.lances.append(lance_usuario_a)
leilao.lances.append(lance_usuario_b)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de R$ {lance.valor}')

avaliador = Avaliador()
avaliador.avaliar(leilao)

print(f'O menor lance foi de R$ {avaliador.menor_lance} e o maior lance foi de R$ {avaliador.maior_lance}.')
