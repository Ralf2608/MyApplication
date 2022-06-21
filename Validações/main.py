import requests
from CEP import BuscaEndereço

cep = '01001000'
objeto_cep = BuscaEndereço(cep)

bairro, localidade, uf = objeto_cep.acesso()

print(bairro, localidade)
