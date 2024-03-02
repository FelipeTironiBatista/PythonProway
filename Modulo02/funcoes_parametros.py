def dados(nome, sobrenome, apelido, qtde_filhos = 0, email= ""):
    print(nome)
    print(apelido)
    print(sobrenome)
    print(qtde_filhos)
    if(email != ""):
        print(email)
        return #Atencao ao uso do return - ele pode impactar no funcionamento da regra.
    print("Email nao informado")

def msg():
    print("Ola mundo")
    
def proway():
    print("Proway")
    
def parametro(valor = ""):
    print(valor)
    
def argumentos(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)
    

dados("Juca","Silva","Juquinha",5)  
dados("Maria","Souza","mariazinha",0,"maria.souza@gmail.com")
# msg()
# proway()
# parametro()
# argumentos()