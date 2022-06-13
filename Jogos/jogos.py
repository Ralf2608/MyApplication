import forca
import adivinhacao

def escolha_jogo():
    print("Escolha o seu jogo: ")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Qual o jogo?\n"))

    if(jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação!")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()