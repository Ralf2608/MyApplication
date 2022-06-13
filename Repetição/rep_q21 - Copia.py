num = int(input("Digite um número:\n"))
primos = [1]
cont = 0

for i in range(2,num):
    divisivel = False
    for p in primos[1:]:
        if i % p == 0:
            cont += 1
            divisivel = True
            break
    if divisivel == False:
        primos.append(i)       
print(primos)
print(cont)

