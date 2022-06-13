from collections import Counter

texto = "Bom dia, meu nome é Rafael!"
minusculo = texto.lower()
frequencia = Counter(minusculo)

print(frequencia)