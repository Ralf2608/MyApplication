lista = []

for i in range(50):
    nm = input("Escreva um número:\n")
    lista.append(nm)

for i in range(50):
    if int(lista[i]) % 2 != 0:
        print(lista[i])
    else:
        pass 