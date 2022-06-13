import pandas as pd

dataset = pd.read_csv('db.csv', sep= ';', index_col= 0)

#Utilizando o método query:
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))

exit()
#Passando mais de um parâmetro:
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])

exit()
#Queries com DataFrame:
select = dataset.Motor == 'Motor Diesel'

print(dataset[select])