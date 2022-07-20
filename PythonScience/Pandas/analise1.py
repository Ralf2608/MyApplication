import pandas as pd

# Apresentação dos tipos das variáveis e quantidade de variáveis no banco de dados:

dados = pd.read_csv('aluguel.csv', sep=';')
tipo = pd.DataFrame(dados.dtypes, columns= ['Tipos de Dados'])
tipo.columns.name = 'Variáveis'
tamanho = dados.shape
index = ['Registro (Imóveis)', 'Variáveis']
tamanho = pd.DataFrame(tamanho, index, columns= ['Quantidade'])

print(f'A base de dados possui:\n{tamanho}')
