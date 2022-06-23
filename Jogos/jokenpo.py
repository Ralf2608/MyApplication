from random import randint
from time import sleep

def jogar():
    opcao = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0,2)

    print('''Suas opções são:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    ''')

    jogador = int(input('Qual a sua jogada?\n'))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(2)
    print('-='*11)

    print(f'Computador jogou: {opcao[computador]}')
    print(f'Você jogou: {opcao[jogador]}')
    print('-='*11)

    #Computador jogou pedra:
    if computador == 0:
        if jogador == 0:
            print('Empatou!')
        elif jogador == 1:
            print('Você venceu!')
        elif jogador == 2:
            print('Você perdeu!')
        else:
            print('Jogada inválida!')

    #Computador jogou papel:
    if computador == 1:
        if jogador == 0:
            print('Você perdeu!')
        elif jogador == 1:
            print('Empatou!')
        elif jogador == 2:
            print('Você ganhou!')
        else:
            print('Jogada inválida!')

    #Computador jogou tesoura:
    if computador == 2:
        if jogador == 0:
            print('Você ganhou!')
        elif jogador == 1:
            print('Você perdeu!')
        elif jogador == 2:
            print('Empatou!')
        else:
            print('Jogada inválida!')

if (__name__ == '__main__'):
    jogar()