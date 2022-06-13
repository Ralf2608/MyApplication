cont = 0
n = float(input("Valor do pão:\n"))
print("Preço do pão - R$",n)
print("Loja Quase Dois - Tabela de Preços")
for i in range(50):
    cont += n 
    print(str(i+1), " - R$ %.2f" %cont)
