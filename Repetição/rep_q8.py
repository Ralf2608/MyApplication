lista = []

for i in range(5):
    num = float(input("Digite um número:\n"))
    lista.append(num)

soma = float(lista[0])+float(lista[1])+float(lista[2])+float(lista[3])+float(lista[4])
media = (float(lista[0])+float(lista[1])+float(lista[2])+float(lista[3])+float(lista[4]))/5

print("A soma é:",soma)
print("A média é:",media)