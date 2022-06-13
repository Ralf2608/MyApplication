n = int(input("Montar tabuada de: "))
ini = int(input("Começa por: "))
fim = int(input("Termina em: "))
while ini>fim:
    print("Valor inválido! Início maior que o fim!")
    ini = int(input("Começa por: "))
    fim = int(input("Termina em: "))
print("Montar tabuada de:",n)
print("Começa por:",ini)
print("Termina em:",fim)
print("Vou montar uma tabuada de",n, "começando em",ini,"e terminando em",fim,":")
for i in range(ini,fim+1):
    mult = n*i
    print(str(n)+" X "+ str(i)+" = "+str(mult))