import pandas as pd

# Apresentação de uma variável e retirada de duplicatas:

dados = pd.read_csv('aluguel.csv', sep= ';')
tipo_imovel = dados['Tipo']
sem_duplicata = tipo_imovel.drop_duplicates()

# Organizando a visualização dos dados:

sem_duplicata = pd.DataFrame(sem_duplicata)
sem_duplicata.index = range(sem_duplicata.shape[0])
sem_duplicata.columns.name = 'Id'

print(sem_duplicata)