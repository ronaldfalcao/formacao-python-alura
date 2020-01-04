def jogar():
    print(29 * "*")
    print("* Bem Vindo ao Jogo da Forca *")
    print(29 * "*")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Qual a letras? ")
        chute = chute.strip()  # Removendo os espaços em branco

        index = 0

        for letra in palavra_secreta:

            if chute.upper() == letra.upper():
                print(f'Encontrei a letra {letra} no índice {index}')
                
            index = index + 1

        print("Jogando...")
    print("Fim do Jogo.")


# Permite rodar no terminal
if __name__ == '__main__':
    jogar()
