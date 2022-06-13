cod = 1
peso = []
altura = []
codigo = []
n = 0
while cod >= 1:
    pes = float(input("Informe a massa desse aluno:\n"))
    alt = float(input("Informa a altura desse aluno:\n"))
    codigo.append(cod)
    peso.append(pes)
    altura.append(alt)
    n += 1
    cod = int(input("Digite o código do aluno:\n"))

maior = None
menor = None
leve = None
pesado = None
dmaior = None
dmenor = None
dleve = None
dpesado = None
sa = 0
sp = 0
for i in range(n):
    if i == 0:
        maior = float(altura[i])
        menor = float(altura[i])
        dmaior = int(codigo[i])
        dmenor = int(codigo[i])
    if float(altura[i]) > maior:
        maior = float(altura[i])
        dmaior = int(codigo[i])

    elif float(altura[i]) < menor:
        menor = float(altura[i])
        dmenor = int(codigo[i])
    sa += float(altura[i])

for i in range(n):
    if i == 0:
        leve = float(peso[i])
        pesado = float(peso[i])
        dleve = int(codigo[i])
        dpesado = int(codigo[i]) 
    if float(peso[i]) > pesado:
        pesado = float(peso[i])
        dpesado = int(codigo[i])

    elif float(peso[i]) < leve:
        leve = float(peso[i])
        dleve = int(codigo[i])
    sp += float(peso[i])


print("O aluno maior é:", str(dmaior)+ " - "+str(maior))
print("O aluno menor é:", str(dmenor)+ " - "+str(menor))
print("O aluno pesado é:", str(dpesado)+ " - "+str(pesado))
print("O aluno leve é:", str(dleve)+ " - "+str(leve))
print("A média das alturas é: %.2f" %(sa/n))
print("A média dos pesos é: %.2f" %(sp/n))