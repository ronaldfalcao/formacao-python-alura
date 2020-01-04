print(36 * '*')
print("* Bem Vindo ao Jogo da Adivinhação *")
print(36 * '*')

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou", chute)

if numero_secreto == chute:
    print("Você Acertou!!!")
else:
    print("Você Errou!!!")
