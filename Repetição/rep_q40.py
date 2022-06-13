codigo = []
veiculos = []
acidentes = []

for i in range(5):
    codigo.append(i+1)
    v = int(input("Quantos veículos?\n"))
    veiculos.append(v)
    a = int(input("Quantos acidentes?\n"))
    acidentes.append(a)

maior = None
menor = None
cmaior = None
cmenor = None
soma = 0
for i in range(5):
    if i == 0:
        maior = int(acidentes[i])     
        menor = int(acidentes[i])
        cmaior = int(codigo[i])
        cmenor = int(codigo[i])
    if int(acidentes[i]) > maior:
        maior = int(acidentes[i])
        cmaior = int(codigo[i])
    elif int(acidentes[i]) < menor:
        menor = int(acidentes[i])
        cmenor = int(codigo[i])
    soma += int(veiculos[i])

print("A cidade com maior número de acidentes é: ",str(cmaior)+ " - "+str(maior)+" acidentes.")
print("A cidade com menor número de acidentes é: ",str(cmenor)+ " - "+str(menor)+" acidentes.")
print("A média de veículos é de: %.1f" %(soma/5))

exc = 0
n = 0
for i in range(5):
    if int(veiculos[i]) < 2000:
        exc += int(acidentes[i])
        n += 1

print("A média de acidentes nas cidades com menos de 2000 veículos é de: %.1f" %(exc/n))
