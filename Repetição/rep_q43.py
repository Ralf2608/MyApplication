resposta = 'S'
lista = ['S','s']
quantidade = []
cont = 1
ordem = []
valorC = 0
valorB = 0
valorBO = 0
valorH = 0
valorCH = 0
valorR = 0
while resposta in lista:
    codigo = int(input("Qual o código do lanche?\n"))
    n = int(input("Quantos deseja?\n"))
    if codigo == 100:
        valorC = n*1.20
        quantidade.append(str(codigo)+": "+str(n)+" ---> R$ "+str(valorC))
    elif codigo == 101:
        valorB = n*1.30
        quantidade.append(str(codigo)+": "+str(n)+" ---> R$ "+str(valorB))
    elif codigo == 102:
        valorBO = n*1.50
        quantidade.append(str(codigo)+": "+str(n)+" ---> R$ "+str(valorBO))
    elif codigo == 103:
        valorH = n*1.20
        quantidade.append(str(codigo)+": "+str(n)+" ---> R$ "+str(valorH))
    elif codigo == 104:
        valorCH = n*1.30
        quantidade.append(str(codigo)+": "+str(n)+" ---> R$ "+str(valorCH))
    elif codigo == 105:
        valorR = n*1.00
        quantidade.append(str(codigo)+": "+str(n)+" ---> R$ "+str(valorR))
    resposta = input('Deseja fazer outro pedido? (S-sim; N-não)\n')

total = valorC+valorB+valorBO+valorH+valorCH+valorR
for i in quantidade:
    print(i)
print("O total da compra foi de: R$",total)
