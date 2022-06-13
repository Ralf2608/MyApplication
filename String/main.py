url = 'https://bytebank.com/cambio?moedaDestino=real&moedaOrigem=dolar&quantidade=100'

#Sanitização da URL:
url = url.strip()

#Validação da URL:
if url == '':
    raise ValueError('A URL estpa vaza.')

#Separa a base e os parâmetros:
indice = url.find('?')
url_base = url[:indice]
url_parametros = url[indice+1:]

#Busca o valor de um parâmetro:
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
limite = url_parametros.find('&', indice_valor)

if limite == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:limite]

print(valor)

