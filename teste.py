from numpy import split


palavra1 = 'Brasil Hexa 2006'
palavra2 = 'Brasil Hexa 2006'
palavra3 = 'Rafael'
if len(palavra1) == len(palavra2):
    print("As palavras possuem mesmo tamanho!")
else:
    print('As palavras não possuem mesmo tamanho!')

if palavra1 == palavra2:
    print('São iguais!')
else:
    print('Não são iguais!')

lista = []
for letra in palavra3.strip():
    lista.append(letra)
    print(lista)