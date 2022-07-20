import pandas as pd

# Seleções e frequências:

dados = pd.read_csv('aluguel_residencial.csv', sep= ';')

# Seleção dos imóveis tipo apartamento:

apto = ['Apartamento']
verificacao = dados['Tipo'].isin(apto)

dados_apto = dados[verificacao]
dados_apto.index = range(dados_apto.shape[0])
n1 = dados_apto.shape[0]

# Seleção dos imóveis tipo casa, casa condomínio e casa vila:

residencia = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
verificacao2 = dados['Tipo'].isin(residencia)

dados_residencia = dados[verificacao2]
dados_residencia.index = range(dados_residencia.shape[0])
n2 = dados_residencia.shape[0]

# Seleção dos imóveis de área entre 60 e 100 m^2:

area = (dados['Area'] >= 60) & (dados['Area'] <= 100)
dados_area = dados[area]
dados_area.index = range(dados_area.shape[0])
n3 = dados_area.shape[0]

# Seleção dos imóveis que tenham pelo menos 4 quartos e aluguel menor que 2000 reais:

selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
dados_selecao = dados[selecao]
dados_selecao.index = range(dados_selecao.shape[0])
n4 = dados_selecao.shape[0]

print(f'N° de imóveis tipo apartamento: {n1}\n'
      f'N° de imóveis tipo casa, casa condomínio e casa vila: {n2}\n'
      f'N° de imóveis de área entre 60 e 100 m^2: {n3}\n'
      f'N° de imóveis que tenham pelo menos 4 quartos e aluguel menor que 2000 reais: {n4}')