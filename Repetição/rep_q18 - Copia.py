N = int(input("Quantos números queres?\n"))
lista = []
maior = None
menor = None

for i in range(N):
    nm = float(input("Digite um número:\n"))
    while nm < 0 or nm > 100:
        print("Digite outro número!")
        nm = float(input("Digite um número:\n"))
    lista.append(nm)

for n in range(N):
    if n == 0:
        maior = float(lista[n])
        menor = float(lista[n])
    elif float(lista[n])>maior:
        maior = float(lista[n])
    else:
        menor = float(lista[n])
print("Maior número\n",maior)
print("Menor número:\n",menor)
soma = float(maior) + float(menor)
print("Soma:\n",soma)