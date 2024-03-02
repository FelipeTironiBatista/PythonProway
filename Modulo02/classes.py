class Principal:
    
    def metodo_principal(self):
        print("Eu sou o método principal da classe Principal")
    
class Principal2:
    
    def metodo_principal(self):
        print("Eu sou o método principal da classe Principal 2")

class Herdeira(Principal, Principal2):
    
    def metodo_principal(self):
        #Principal.metodo_principal(self)
        #Principal2.metodo_principal(self)
        super().metodo_principal()
        super(Principal, self).metodo_principal()
        
obj = Herdeira()
# print(Herdeira.mro())
# print(Herdeira.__mro__)
obj.metodo_principal()
