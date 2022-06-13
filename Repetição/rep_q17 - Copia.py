n = int(input("Dê-me um número:\n"))
anterior = 1

while n <= 0 or n>16:
    print("Número inválido! Tente novamente.")
    n = int(input("Dê-me um número:\n"))

for i in range(n):
    fat = (i+1)*anterior
    anterior = fat
print(anterior)

resp = input("Deseja fazer um novo processo? (S-sim, N-não)")
while resp == "S":
    n = int(input("Dê-me um número:\n"))
    anterior = 1
    
    while n <= 0 or n>16:
        print("Número inválido! Tente novamente.")
        n = int(input("Dê-me um número:\n"))

    for i in range(n):
        fat = (i+1)*anterior
        anterior = fat
    print(anterior)