class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f'Código {self.codigo}\nValor {self.saldo}'

conta1 = ContaCorrente(15)
conta1.deposita(500)

conta2 = ContaCorrente(47685)
conta2.deposita(1000)

contas = [conta1, conta2]
for conta in contas:
    print(conta)