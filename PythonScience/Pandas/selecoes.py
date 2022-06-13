import pandas as pd

dataset = pd.read_csv('db.csv', sep= ';', index_col= 0)

#Utilizando o .iloc para seleções:
print(dataset.iloc[[1]])

exit()
#Utilizando .loc para seleções:
#Para retorna mais de uma informação:
print(dataset.loc[["Passat", "DS5"], ['Motor', 'Valor']])

exit()

print(dataset.loc["Passat"])

exit()
#Selecionando linhas:
print(dataset[0:3])

exit()
#Selecionando colunas:
#Retorna uma Series
print(dataset['Valor'])

exit()
#Retorna um DataFrame
print(dataset[['Valor']])