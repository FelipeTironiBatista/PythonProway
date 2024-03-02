class Veiculos:
#Atributos
    # cor = 'Branco'
    # ligado = False
    
#Metodos
    def __init__(self, pCor, pLigado = False):
        self.cor = pCor
        self.ligado = False

    def ligar(self):
        if(self.ligado):
            print("O carro já está ligado")
            return
        self.ligado = True
        print('O carro foi ligado')
    
    def desligar(self):
        if(not (self.ligado)):
            print("O carro já está desligado")
            return
        self.ligado = False
        print("O carro foi desligado")
        
#Instanciar um objeto - criar um objeto
# carro = Veiculos()
# #print(carro.cor)
# print(carro.ligado)
# #Invocando um metodo da classe
# carro.ligar()
# print(carro.ligado)
# carro.desligar
# print(carro.ligado)

# carro = Veiculos("Preto")   
# print(carro.cor)
# print(carro.ligado)

# carro2 = Veiculos("Branco") #Nascendo cor preto
# print(carro2.cor)
# print(carro2.ligado)

# carro3 = Veiculos("Azul")
# print(carro3.cor)
# print(carro3.ligado)

class Carro(Veiculos):
    def marchaRe(self):
        print("Engatou a marcha ré")

gol = Carro("Amarelo")
print(gol.ligado)
gol.marchaRe()

class Moto(Veiculos):
    def pezinho(self):
        print("Botou a moto no pezinho")
        
cg = Moto("Azul")
print(cg.ligado)
cg.pezinho()