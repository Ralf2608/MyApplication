import forca
import adivinhacao
import jokenpo

def escolha_jogo():
    print("Escolha o seu jogo: ")

    print("(1) Forca\n(2) Adivinhação\n(3) Jokenpô")

    jogo = int(input("Qual o jogo?\n"))

    if(jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação!")
        adivinhacao.jogar()
    elif(jogo == 3):
        print('Jogando Jokenpô')
        jokenpo.jogar()

if(__name__ == "__main__"):
    escolha_jogo()