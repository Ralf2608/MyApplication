A = float(input("Número de habitantes em A:\n"))
B = float(input("Número de habitantes em B:\n"))

ano = 0
while A < B:
    A = A*1.03
    B = B*1.015
    ano = ano + 1

print("O ano em que A passa B é:\n",ano)