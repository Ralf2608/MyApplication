import pandas as pd

dados = pd.read_csv('aluguel_residencial.csv', sep= ';')

''' A função isnull() indica os valores NaN (True) e a função notnull()
    indica os valores que não são NaN.
    Identificando os valores NaN:
'''
dados[dados['Valor'].isnull()]
A = dados.shape[0]
dados.dropna(subset= ['Valor'], inplace= True)
B = dados.shape[0]

# Tratamento de dados faltantes:

selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())
dados = dados[~selecao]
C = dados.shape[0]

# Removendo os valores nulos (fillna() remove os valores nulos adicionando o valor desejado):
dados = dados.fillna({'Condominio':0, 'IPTU':0})

dados.to_csv('aluguel_residencial.csv', sep= ';', index= False)