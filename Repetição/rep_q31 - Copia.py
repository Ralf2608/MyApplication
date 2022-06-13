valor = float(input("Qual o valor?\n"))
produto = []
while valor != 0:
    produto.append(valor)
    valor = float(input("Qual o valor?\n"))

print("Lojas Tabajara")
cont = 0
for i in produto:
    cont += 1
    print("Produto "+str(cont)+": R$ "+ str(i))

total = 0
for i in produto:
    total += float(i)
print("Total: R$",total)
dinheiro = float(input("Dinheiro: R$ "))
print("Troco: R$",(dinheiro-total))
