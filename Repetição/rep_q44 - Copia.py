resp = 'S'
lista = ['S','s']
i = 0
j = 0
k = 0
l = 0
m = 0
o = 0
total = 0

while resp in lista:
    n = int(input("Em quem você vota?\n1 - José\n2 - João\n3 - Cláudia\n4 - Marcela\n5 - Voto Nulo\n6 - Voto em Branco\n"))
    if n == 1:
        i+=1
    elif n == 2:
        j +=1
    elif n == 3:
        k +=1
    elif n == 4:
        l +=1
    elif n == 5:
        m +=1
    elif n == 6:
        o +=1
    total += 1
    resp = input("Deseja votar novamente? (S-sim; N-não)\n")
print("José obteve: "+str(i)+" votos.")
print("João obteve: "+str(j)+" votos.")
print("Cláudia obteve: "+str(k)+" votos.")
print("Marcela obteve: "+str(l)+" votos.")
print("Votos nulos:",m)
print("Votos em branco:",o)
print("A porcentagem de votos nulos é: %.2f" %((m/total)*100))
print("A porcentagem de votos em branco é: %.2f" %((o/total)*100))