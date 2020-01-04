

print(36 * '*')
print("* Bem Vindo ao Jogo da Adivinhação *")
print(36 * '*')

numero_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):

    print("Rodada {} de {}.".format(rodada, total_tentativas))  # string interpolation
    chute = int(input("Digite o seu número: "))

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue

    print("Você digitou", chute)

    acertou = numero_secreto == chute
    errou_chute_menor = numero_secreto > chute
    errou_chute_maior = numero_secreto < chute

    if acertou:
        print("Você Acertou!!!")
        break
    else:
        if errou_chute_menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")
        elif errou_chute_maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
