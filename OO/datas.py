class Data:

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        return ("{}/{}/{}".format(self.dia,self.mes,self.ano))

hoje = Data(5,5,2022)
print(hoje)