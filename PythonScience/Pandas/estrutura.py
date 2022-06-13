import pandas as pd

#Criando um DataFrame a partir de um arquivo externo
dataset = pd.read_csv('db.csv', sep= ';', index_col= 0)
#A opção index_col= 0 indica qual coluna deve ser assumida como índice

print(dataset)

exit()
#Criando um DataFrame a partir de uma lista de dicionários
dados1 = [{'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2007, 'Quilometragem':44420.0, 'Zero_km': False, 'Valor': 88078.64},
         {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1993, 'Quilometragem':5732.0, 'Zero_km': False, 'Valor': 106161.94},
         {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem':37123.0, 'Zero_km': False, 'Valor': 72832.16}
         ]

dados2 = {'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
          'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
          'Ano': [2007, 1993, 1990],
          'Quilometragem': [44420.0, 5732.0, 37123.0],
          'Zero_km': [False, False, False],
          'Valor': [88078.64, 106161.94, 72832.16]
         }

#dataset1 = pd.DataFrame(dados1)
#print(dataset1)

dataset2 = pd.DataFrame(dados2)
print(dataset2)

exit()
#Criando uma Series a partir de uma lista
carros = ['Jetta Variant', 'Passat', 'Crossfox']
print(pd.Series(carros))
