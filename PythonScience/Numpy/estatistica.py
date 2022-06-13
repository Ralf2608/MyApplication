import numpy as np

anos = np.loadtxt('carros-anos.txt', dtype= int)
km = np.loadtxt('carros-km.txt')
valor = np.loadtxt('carros-valor.txt')

#Criação de uma matriz com 3 colunas juntando os 3 arrays anteriores:
dataset = np.column_stack((anos, km, valor))

print('A média da quilometragem é',np.mean(dataset[:,1]))
print('O desvio padrão da quilometragem é',np.std(dataset[:,1]))
print('A quilometragem total é {} km.'.format(dataset[:,1].sum()))