el = int(input("Número de eleitores:\n"))

votoA = ['A','a']
votoB = ['B','b']
votoC = ['C','c']
a = 0
b = 0
c = 0

for i in range(el):
    voto = input("Em quem você vota? (A, B ou C)\n")
    if voto in votoA:
        a += 1
    elif voto in votoB:
        b += 1
    elif voto in votoC:
        c += 1

print("Candidato A:\n",a)
print("Candidato B:\n",b)
print("Candidato C:\n",c)
