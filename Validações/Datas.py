from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.cadastro = datetime.today()

    def __str__(self):
        return f'{self.format()}\nTempo de cadastro: {self.tempo_cadastro()}'

    def dia(self):
        dia = str(self.cadastro.day)
        return dia
    
    def mes(self):
        meses = [
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
            'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
                ]
        mes_cadastro = self.cadastro.month
        return meses[mes_cadastro-1]
    
    def ano(self):
        ano = str(self.cadastro.year)
        return ano

    def dia_semana(self):
        semana = [
            'segunda', 'terça', 'quarta',
            'quinta', 'sexta', 'sábado',
            'domingo'
                 ]
        dia_semana = self.cadastro.weekday()
        return semana[dia_semana]

    def format(self):
        formato = self.cadastro.strftime('%d/%m/%Y %H:%M')
        return formato

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=15, minutes=20, seconds=30)) - self.cadastro
        return tempo_cadastro