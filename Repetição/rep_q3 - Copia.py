nome = (input("Digite seu nome:\n"))
idade = float(input("Qual a sua idade?\n"))
salario = float(input("Quanto recebe?\n"))
sexo = input("Qual o sexo? (f- feminino ou m- masculino)\n") 
estado = input("Estado civil? (s, c, v, d)\n")

while len(nome)<3:
    print("Digite um nome com mais de 3 caracteres.")
    nome = input("Digite seu nome:\n")

while idade<0 or idade>150:
    print("Idade inválida. Tente novamente.")
    idade = input("Qual a sua idade?\n")

while salario<0:
    print("Salário inválido.")
    salario = input("Quanto recebe?\n")

while sexo != "f" and sexo != "m":
    print("Sexo inválido.")
    print(sexo)
    sexo = input("Qual o sexo? (f- feminino ou m- masculino)\n") 

while estado!="s" and estado!="c" and estado!="v" and estado!="d":
    print("Estado civil inválido.")
    estado = input("Estado civil? (s, c, v, d)\n")

