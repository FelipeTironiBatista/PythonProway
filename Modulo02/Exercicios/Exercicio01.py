# Elaborar um algoritmo para manipulacao de um banco
# A classe deverá se chamar ContaBancaria
# Toda conta deverá iniciar com saldo zerado
# Deverao ser implementados os métodos (sacar, ver saldo, transferir, depositar)
# - Somente podera sacar se tiver saldo suficiente
# - Transferencias, deverão ser autorizadas apenas para contas com numero de 5 digitos desde que haja saldo suficiente
# - Nao sera permitido transferencia para a mesma conta

# Deverao ser implementadas herancas para contas (Corrente / Poupanca / Salario)
# - Conta Corrente deverá ter uma taxa 5% do valor do saque.
# - Conta Salario nao podera depositar

# Todos os metodos deverao possuir retorno informando ao usuario o que foi feito e tratadas as eventuais situacoes

#Implementar um menu eletronico


# conta = input("Informe os dados da sua conta: ")
# print("Informe o tipo da conta: ")
# tpConta = input("1-Corrente \n2-Poupanca \n3-Salario \n")

# oper = 0
# while oper != '5':
#     print("Selecione a operação")
#     oper = input("1-Saque \n2-Consulta de Saldo \n3-Transferência \n4-Depósito \n5-Sair \n")

# exit
 
class ContaBancaria:
    def __init__(self, numero):
        self.saldo = 0
        self.numero = numero

    def existeSaldo(self, valor):
        return valor <= self.getSaldo()
    
    def getSaldo(self):
        return self.saldo
    
    def verSaldo(self):
        print(f"Saldo atual: {self.getsaldo()}")
        
    def transferir(self, valor):
        destino = input("Informe a conta destino: ")
        if (len(destino) != 5):
            print("Formato de conta inválido")
            return
        if (destino == self.numero):
            print("Conta destino não pode ser a mesma conta atual")
            return
        if (not (self.existeSaldo(valor))):
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        print("Transferencia efetuada com sucesso")
 
                
        
        
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        total = valor + (valor * 0.05)
        if (self.existeSaldo()):
            self.saldo += valor
            print("Saque efetuado com sucesso!")
            return
        print("Saldo insuficiente!")
        
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso")
        
class ContaSalario(ContaBancaria):
    def sacar(self, valor):
        if (self.existeSaldo()):
            self.saldo += valor
            print("Saque efetuado com sucesso!")
            return
        print("Saldo insuficiente!")
      

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if (self.existeSaldo()):
            self.saldo += valor
            print("Saque efetuado com sucesso!")
            return
        print("Saldo insuficiente!")
        
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso")
     
       
numero = int(input("Informe o numero"))
if (numero <= 0):
    print("Necessario ser positivo")
else:
    conta = ContaBancaria(numero)
    print(conta.numero)
print(conta)
        
    
    




    
    
