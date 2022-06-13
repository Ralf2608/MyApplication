import pandas as pd

dataset = pd.read_csv('db.csv', sep= ';', index_col= 0)

#Função .dropna() elimina os valores nulos:
dataset.dropna(subset= ['Quilometragem'], inplace= True)

print(dataset)

exit()
#Função .fillna() preenche os valores nulos com um valor definido. Com o inplace= True os valores são substituídos nos dados:
dataset.fillna(0, inplace= True)
print(dataset.query('Zero_km == True'))

exit()
#Função .isna() identifica os valores nulos e imprime em booleano:
print(dataset.Quilometragem.isna())

exit()
#A função .info() imprime as informações das colunas, porém elimina as informações nulas:
dataset.info()

exit()
#Função iterrows gera tuplas de acordo com o nome de cada linha, onde a tupla vai compor do nome da linha com o os dados restantes para essa linha
for index , row in dataset.iterrows():
    if(2019 - row['Ano'] != 0):
        dataset.loc[index, "km_media"] = row['Quilometragem'] / (2019 - row['Ano'])
    else:
        dataset.loc[index,"km_media"] = 0

print(dataset)