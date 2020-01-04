print(36 * '*')
print("* Bem Vindo ao Jogo da Adivinhação *")
print(36 * '*')

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou", chute)

acertou = numero_secreto == chute
errou_chute_menor = numero_secreto > chute
errou_chute_maior = numero_secreto < chute

if acertou:
    print("Você Acertou!!!")
else:
    if errou_chute_menor:
        print("O seu chute foi menor do que o número secreto!")
    elif errou_chute_maior:
        print("O seu chute foi maior do que o número secreto!")
