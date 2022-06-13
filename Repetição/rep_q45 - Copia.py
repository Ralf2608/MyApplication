gabarito = ['A','B','C','D','E','E','D','C','B','A']
cont = 0
resposta = 'S'
lista = ['S','s']
notas = []
total = 0
while resposta in lista:
    for i in range(10):
        resp = input("Qual a letra que você marcou?\n")
        if resp in gabarito[i]:
            cont += 1
    notas.append(cont)
    total += 1
    resposta = input("Outro aluno deseja utilizar? (S-sim; N-não)\n")
    cont = 0

maior = None
menor = None
soma = 0
for i in range(total):
    if i == 0:
        maior = int(notas[i])
        menor = int(notas[i])
    if int(notas[i])>maior:
        maior = int(notas[i])
    elif int(notas[i])<menor:
        menor = int(notas[i])
    soma += int(notas[i])
print("A maior pontuação foi:",maior)
print("A menor pontuação foi:",menor)
print("O total de alunos foi:",total)
print("A média da turma é: %.2f" %(soma/total))
print("Gabarito da prova:")
for i in range(10):
    if i< 9:
        print("0"+str(i+1)+" - "+gabarito[i])
    elif i == 9:
        print(str(i+1)+" - "+gabarito[i])