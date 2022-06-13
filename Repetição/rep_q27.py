t = int(input("Quantas turmas?\n"))
turma = []

for i in range(t):
    nm = int(input("Quantos alunos possuem?\n"))
    while nm>40:
        print("Quantidade inválida!")
        nm = int(input("Quantos alunos possuem?\n"))
    turma.append(nm)

soma = 0
for i in range(t):
    soma += int(turma[i])

print("A média de alunos por turma é:\n",(soma/t))