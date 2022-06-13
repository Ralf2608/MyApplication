b = int(input("Digite a base:\n"))
e = int(input("Digite o expoente:\n"))

res = 1
for i in range(e):
    res = res*b

print(str(b)+"^"+str(e)+" = "+str(res))