import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia.')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio') 
        match = padrao_url.match(url)

        if not match:
            raise ValueError('A URL não é válida.')

    def get_url_base(self):
        indice = self.url.find('?')
        url_base = self.url[:indice]
        return url_base

    def get_url_parametros(self):
        indice = self.url.find('?')
        url_parametros = self.url[indice+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        limite = self.get_url_parametros().find('&', indice_valor)

        if limite == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:limite]
        return valor

    def conversao(self):
        origem = self.get_valor_parametro('moedaOrigem')
        quantidade = float(self.get_valor_parametro('quantidade'))
        cambio = 5.5

        if origem == 'real':
            valor_conv = quantidade/cambio
        else:
            valor_conv = quantidade*cambio
        
        return valor_conv

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_parametros + '\n' + 'URL Base: ' + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url

url = 'https://bytebank.com/cambio?moedaDestino=real&moedaOrigem=dolar&quantidade=100'
extrator_url = ExtratorURL(url)
conv = extrator_url.conversao()
print(conv)