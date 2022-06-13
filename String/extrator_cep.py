endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, Rj, 23440120'

import re #Regular Expression -- RegEx

# CEP = 5 dígitos + hífen (opcional) + 3 dígitos:

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco) #retorna o match
if busca:
    cep = busca.group() #retorna a string encontrada no endereço
    print(cep)