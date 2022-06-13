n = int(input("Indique quantas temperaturas vão ser analisadas:\n"))
lista = []
soma = 0
for i in range(n):
    temp = float(input("Qual a temperatura?\n"))
    lista.append(temp)
    soma += temp

maior = None
menor = None
for i in range(n):
    if i == 0:
        maior = float(lista[i])
        menor = float(lista[i])
    if float(lista[i]) > maior:
        maior = float(lista[i])
    elif float(lista[i]) < menor:
        menor = float(lista[i])

print("A menor temperatura é:",menor)
print("A maior temperatura é:",maior)
print("A média das temperaturas é: %.2f" %(soma/n))