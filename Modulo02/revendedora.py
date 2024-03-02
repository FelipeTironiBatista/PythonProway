class Veiculo:
    def __init__(self, cor, ano, possuiRe = True):
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.marcha = 0
        self.marchaTotal = 5
        self.possuiRe = possuiRe
        
    def ligar(self):
        if (self.ligado):
            return 'O veiculo ja esta ligado'
        self.ligado = True
        return 'O veiculo foi ligado'
    
    def desligar(self):
        if (self.marcha != 0):
            return 'O veiculo somente podera ser desligado estando no Neutro'
        if (not(self.ligado)):
            return 'O veiculo ja esta desligado'
        self.ligado = False
        return 'O veiculo foi desligado'
       
    def acelerar(self):
        if (self.ligado):
            if (self.marcha == self.marchaTotal):
                return f'O veiculo ja esta na marcha {self.marchaTotal}'
            self.marcha += 1
            return f'Marcha {self.marcha}'
        return 'O veiculo esta desligado'
                
    def reduzir(self):
        if (self.__class__.__name__ == 'Moto'):
            return 'Nao existe marcha re'
        if (self.ligado):
            if (self.marcha < 0):
                return 'Veiculo ja esta na Marcha re'
            if (self.marcha >= 0):
                self.marcha -= 1
                if (self.marcha > 0):
                    return f'Marcha {self.marcha}'
                if (self.marcha == 0):
                    return 'Neutro'
                if (self.marcha < 0):
                    return 'Marcha re'
        return 'O veiculo esta desligado'

        
class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass



# falcon = Moto('Cinza', 2024)
# print(falcon.ligar())
# print(falcon.reduzir())
# print(falcon.reduzir())

# gol = Carro('Preto', 2022)
# print(gol.ligado)
# print(gol.ligar())
# print(gol.ligado)
# print(gol.ligar())
# print(gol.desligar)
# print(gol.ligado)
# print(gol.desligar())
# print(gol.acelerar())
# print(gol.acelerar())
# print(gol.acelerar())
# print(gol.acelerar())
# print(gol.acelerar())
# print(gol.desligar())
# print(gol.acelerar())
# print(gol.reduzir())
# print(gol.reduzir())
# print(gol.reduzir())
# print(gol.reduzir())