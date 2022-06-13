from operator import index


def jogar():
    print("Bem vindo ao jogo de Forca!\n")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual a letra?\n")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index] = letra
                index = index + 1

        else:
            erros = erros + 1
            print("Letra errada! Faltam {} tentativas.".format(6-erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns!\n")
    elif(enforcou):
        print("Você perdeu!\n")
    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()