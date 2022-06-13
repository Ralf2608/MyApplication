from abc import ABCMeta, abstractmethod

class Conta(metaclass = ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'Código {self._codigo}\nSaldo {self._saldo}'

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass


conta1 = ContaCorrente(16)
conta1.deposita(1000)
conta1.passa_o_mes()

conta2 = ContaPoupanca(17)
conta2.deposita(1000)
conta2.passa_o_mes()

contas = [conta1, conta2]
for conta in contas:
    print(conta)