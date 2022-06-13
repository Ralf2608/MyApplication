cd = int(input("Quantos CD's?\n"))
total = 0

for i in range(cd):
    nm = float(input("Quanto custa?\n"))
    total += nm
print("O valor investido total é de:\n",total,"reais")
print("A média investida por CD é:\n",(total/cd),"reais")