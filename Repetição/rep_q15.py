#termo = int(input("Coloque o termo:\n"))
atual = 0
anterior = 0

i = 0
while atual<500:
    if i == 0:
        atual = 0
        i += 1

    elif i == 1:
        atual = 1
        i += 1
    else:
        f2= atual
        atual += anterior
        anterior = f2 
    print(atual)