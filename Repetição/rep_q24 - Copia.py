notas = []
n = int(input("Digite a quantidade de notas:\n"))

for i in range(n):
    nm = float(input("Digite as notas:\n"))
    notas.append(nm)

soma = 0
for i in range(n):
    soma += float(notas[i])
print("A média é:\n", (soma/n))
