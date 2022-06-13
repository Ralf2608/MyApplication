import random
import matplotlib.pyplot as plt

notas = []
random.seed(11)

for nota in range(8):
    notas.append(random.randrange(0,11))

x = list(range(1,9))
y = notas
plt.plot(x,y, marker='o')
plt.title("Notas de Matemática")
plt.xlabel("Provas")
plt.ylabel("Notas")
plt.show()