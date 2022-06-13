divida = float(input("Qual o valor da dívida?\n"))
anterior3 = None
anterior6 = None
anterior9 = None
anterior12 = None

for i in range(3):
    divida3 = divida*1.1
    anterior3 = divida3
parcela3 = divida3/3

for i in range(6):
    divida6 = divida*1.15
    anterior6 = divida6
parcela6 = divida6/6

for i in range(9):
    divida9 = divida*1.2
    anterior9 = divida9
parcela9 = divida9/9

for i in range(12):
    divida12 = divida*1.25
    anterior12 = divida12
parcela12 = divida12/12

for i in range(5):
    if i == 0:
        print("Valor da dívida: R$",divida)
        print("Valor dos juros 0")
        print("Quantidade de parcelas 1")
        print("Valor da parcela: R$",divida)
    elif i == 1:
        print("Valor da dívida: R$",divida3)
        print("Valor dos juros 10%")
        print("Quantidade de parcelas 3")
        print("Valor da parcela: R$ %.2f" %parcela3)
    elif i == 2:
        print("Valor da dívida: R$",divida6)
        print("Valor dos juros 15%")
        print("Quantidade de parcelas 6")
        print("Valor da parcela: R$ %.2f" %parcela6)
    elif i == 3:
        print("Valor da dívida: R$",divida9)
        print("Valor dos juros 20%")
        print("Quantidade de parcelas 9")
        print("Valor da parcela: R$ %.2f" %parcela9)
    elif i == 4:
        print("Valor da dívida: R$",divida12)
        print("Valor dos juros 25%")
        print("Quantidade de parcelas 12")
        print("Valor da parcela: R$ %.2f" %parcela12)
    

