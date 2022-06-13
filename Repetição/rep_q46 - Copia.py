resposta = 'S'
lista = ['S','s']
while resposta in lista:
    nome = input("Qual o nome do atleta?\n")
    saltos = []
    for i in range(5):
        s = float(input("Qual a distância?\n"))
        saltos.append(s)

    maior = None
    menor = None
    
    for i in range(5):
        if i == 0:
            maior = float(saltos[i])
            menor = float(saltos[i])
        if float(saltos[i])>maior:
            maior = float(saltos[i])
        elif float(saltos[i])<menor:
            menor = float(saltos[i])

    print("Atleta:",nome)
    for i in range(5):
        print(str(i+1)+"° salto: "+str(saltos[i])+" m")

    saltos.remove(maior)
    saltos.remove(menor)

    soma = 0
    for i in saltos:
        soma += i

    print("Melhor salto: "+str(maior)+" m")
    print("Pior salto: "+str(menor)+" m")
    print("Média dos demais saltos: %.2f" %(soma/3)+" m")
    print("Resultado final:")
    print(nome,": %.2f" %(soma/3)," m")
    resposta = input("Há outro atleta? (S-sim; N-não)\n")
    