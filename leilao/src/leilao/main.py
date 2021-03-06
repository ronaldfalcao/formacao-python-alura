from leilao.src.leilao.dominio import Lance, Leilao, Usuario

usuario_a = Usuario("A", 500)
usuario_b = Usuario("B", 500)

lance_usuario_a = Lance(usuario_a, 200.0)
lance_usuario_b = Lance(usuario_b, 120.0)

leilao = Leilao("Leilão de Exemplo")

leilao.propor(lance_usuario_a)
leilao.propor(lance_usuario_b)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de R$ {lance.valor}')

print(f'O menor lance foi de R$ {leilao.menor_lance} e o maior lance foi de R$ {leilao.maior_lance}.')
