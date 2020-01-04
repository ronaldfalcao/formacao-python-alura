import forca
import adivinhacao


def escolhe_jogo():
    print(20 * "*")
    print("* Escolha seu Jogo *")
    print(20 * "*")

    print("(1) Forca\t(2) Adivinhação")

    jogo = int(input("Qual deseja jogar? "))

    if jogo == 1:
        print("Jogo da Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogo da Adivinhação")
        adivinhacao.jogar()
    else:
        print("Nenhum jogo selecionado!")


# Permite rodar no terminal
if __name__ == '__main__':
    escolhe_jogo()
