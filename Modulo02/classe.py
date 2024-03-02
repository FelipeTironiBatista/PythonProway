class MinhaClasse:
    #Atributos da classe - caracteristicas
    atributo1 = any
    atributo2 = any
    
    #Metodos da classe - acoes
    
    def __int__(self, parametro): # <-- Método construtor
        self.atributo3 = parametro
        self.atributo4 = None
        self.atributo2 = None #<-- O atributo do método se sobrepoe ao atributo da classe.
        pass   

    def metodo1(self):
        pass
    
    def metodo2(self):
        pass
    
    #Heranca simples
class Herdeira(MinhaClasse):
    pass
    
object = Herdeira()
object.metodo1()