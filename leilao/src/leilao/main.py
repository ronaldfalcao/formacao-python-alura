from dominio import Lance, Leilao, Usuario


usuario_a = Usuario("A")
usuario_b = Usuario("B")

lance_usuario_a = Lance(usuario_a, 100.0)
lance_usuario_b = Lance(usuario_b, 110.0)

leilao = Leilao("Leilão de Exemplo")

leilao.lances.append(lance_usuario_a)
leilao.lances.append(lance_usuario_b)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de R$ {lance.valor}')
