lista = []

for i in range(10):
    nm = input("Digite um número:\n")
    lista.append(nm)

j = 0
m = 0

for n in range(10):
    if int(lista[n]) % 2 == 0:
        j = j + 1
    else:
        m = m + 1

print("Quantidade de pares: ",j)
print("Quantidade de ímpares: ",m)