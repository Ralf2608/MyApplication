salario = float(input("Digite o salário:\n"))
taxa = 0.015
for i in range(4):
    if i == 0:
        salario += salario*taxa
    else:
        imposto = 2*taxa
        salario += salario*imposto
        taxa = imposto 
print("O salário atual é: %.2f" %salario)