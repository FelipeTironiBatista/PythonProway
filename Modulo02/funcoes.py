#Estrutura de uma funcao simples = def / termo reservado
def funcao():
    print("Eu sou uma funcao em Python")
    print("Eu sou a segunda linha da funcao em Python")
    
def funcao2():
    print("Eu sou a funcao 2 em Python")
    print("Sou uma funcao diferente da funcao anterior")

opcao = int(input("Qual funcao deseja executar? 1 ou 2?"))
if ( opcao == 1 ):
    funcao()
else:
    funcao2()

def retorno():
    return "Eu sou uma funcao de retorno"

def compara():
    if(1 ==1):
        return "Valores iguais"

def compara():
    funcao()
    if(1 ==1):
        return "Valores iguais"    
    
# opcao = input("Deseja executar novamente qual funcao? 1 ou 2?")
# if ( opcao == "1"):
#     funcao()
# else:
#     funcao2()
# print(retorno())