def jogar():
    print(29 * "*")
    print("* Bem Vindo ao Jogo da Forca *")
    print(29 * "*")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0
    
    while not enforcou and not acertou:

        chute = input("Qual a letras? ")
        chute = chute.strip().upper()  # Removendo os espaços em branco

        if chute in palavra_secreta:
            index = 0

            for letra in palavra_secreta:

                if chute == letra:
                    print(f'Encontrei a letra {letra} no índice {index}')
                    letras_acertadas[index] = letra

                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        print("Jogando...")

    if acertou:
        print("Você venceu!")
    else:
        print("Você Perdeu!")
        
    print("Fim do Jogo.")


# Permite rodar no terminal
if __name__ == '__main__':
    jogar()
