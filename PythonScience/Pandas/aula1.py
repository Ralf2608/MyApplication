import pandas as pd
#Imprime todas as linhas possíveis
#pd.set_option('display.max_rows', 1000)  
#Imprime todas as colunas possíveis
#pd.set_option('display.max_columns', 1000)  

dataset = pd.read_csv('db.csv', sep = ';')
#Imprime os tipos de dados presentes em cada coluna
#print(dataset.dtypes)
#Imprime um resumo estatístico das colunas selecionadas
#print(dataset[['Quilometragem', 'Valor']].describe())
#imprime as informações do array (não precisa do print)
#dataset.info()