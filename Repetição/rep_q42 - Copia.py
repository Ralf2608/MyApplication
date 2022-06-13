n = float(input("Digite um número positivo:\n"))
i = 0
j = 0
k = 0
l = 0
while n>=0:
    if n>=0 and n<=25:
        i += 1
    elif n>=26 and n<=50:
        j += 1
    elif n>=51 and n<=75:
        k += 1
    elif n>= 76 and n<=100:
        l +=1
    n = float(input("Digite um número positivo:\n"))
    
print("A quantidade de números entre [0-25] é de:",i)
print("A quantidade de números entre [26-50] é de:",j)
print("A quantidade de números entre [51-75] é de:",k)
print("A quantidade de números entre [76-100] é de:",l)