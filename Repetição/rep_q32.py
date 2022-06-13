n = int(input("Dê-me um número:\n"))
anterior = 1
texto = str(n)+"! = "
x = n
for i in range(n):
    if i == (n-1):
        texto += str(x) 
        fat = (i+1)*anterior
        anterior = fat
        break
    fat = (i+1)*anterior
    anterior = fat
    texto += str(x) + "."
    x = x - 1

print("Fatorial de:",n)
print(texto+" = "+str(anterior))

