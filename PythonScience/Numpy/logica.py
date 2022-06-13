import numpy as np

km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1993, 1990, 2019, 2006]

info = km + anos
matriz = np.array(info).reshape((2, 5))

matriz_new = matriz.copy()

matriz_new.resize((3, 5), refcheck = False)
matriz_new[2] = matriz_new[0] / (2020 - matriz_new[1])
print(matriz_new)
