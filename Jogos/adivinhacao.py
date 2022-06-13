import random

def jogar():

    print("################################")
    print("Bem vindo ao jogo de adivinhação")
    print("################################")

    numero_secreto = random.randrange(20,50)
    tentativas = 0
    pontos = 100

    print("Qual nível de dificuldade?\n","(1) Fácil (2) Médio (3) Difícil")

    nivel = float(input("Digite o nível: "))

    if(nivel == 1):
        tentativas = 3
    elif(nivel == 2):
        tentativas = 2
    else:
        tentativas = 1

    for rodada in range(1, tentativas + 1):
        print("Tentativas {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 20 e 50: "))

        if(chute < 20 or chute > 50):
            print("Digite um número entre 20 e 50!")
            continue
        
        if(numero_secreto == chute):
            print("Você acertou e fez {} pontos.".format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print("Você errou para mais.")
            if(chute < numero_secreto):
                print("Você errou para menos.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
    print("O jogo acabou!")

if(__name__ == "__main__"):
    jogar()