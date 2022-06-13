idade = []
p = int(input("Digite o número de pessoas:\n"))

for i in range(p):
    ida = int(input("Qual a idade?\n"))
    idade.append(ida)

soma = 0
for n in range(p):
    soma += int(idade[n])

media = soma/p
if media>0 and media<=25:
    print("População jovem.")

elif media>=26 and media<=60:
    print("População adulta.")

else:
    print("População idosa.")