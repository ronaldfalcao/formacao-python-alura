
import random

print(36 * '*')
print("* Bem Vindo ao Jogo da Adivinhação *")
print(36 * '*')

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000

print("Escolha seu nível de dificuldade:\n", numero_secreto)
print("(1) Fácil\t(2) Médio\t(3)Difícil")
nivel = int(input("Escolha seu nível agora: "))

if nivel == 1:
    total_tentativas = 20
elif nivel == 2:
    total_tentativas = 10
elif nivel == 3:
    total_tentativas = 5
else:
    total_tentativas = 20  # Deixando o nível Fácil como default para qualquer outro valor

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
        print("Vocês fez {}".format(pontos))
        break
    else:
        if errou_chute_menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

            if rodada == total_tentativas:
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

        elif errou_chute_maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")

            if rodada == total_tentativas:
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print("Fim do jogo")
