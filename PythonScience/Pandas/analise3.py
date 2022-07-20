import pandas as pd

# Análise dos imóveis residenciais:

dados = pd.read_csv('aluguel.csv', sep= ';')
imoveis = list(dados['Tipo'].drop_duplicates())
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']

# Criação de uma Serie só com os tipos residenciais:

verificacao = dados['Tipo'].isin(residencial)

# Criação de um novo DataFrame só com os tipos residenciais:

dados_residencial = dados[verificacao]
dados_residencial.index = range(dados_residencial.shape[0])

# Exportando a base de dados:
dados_residencial.to_csv('aluguel_residencial.csv', sep= ';', index = False)
