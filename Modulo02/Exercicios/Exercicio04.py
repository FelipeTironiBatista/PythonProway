#Elaborar um algoritmo que peca 2 valores numericos para o usuario e retorne o resultado 
# a operação aritmetica ATRAVES DE FUNCAO de acordo com o escolhido.
#DEVERA POSSUIR PARAMETROS OPCIONAIS E NAO OPCIONAIS NA FUNCAO
#Tratar divisao por zero
#NOME DA FUNCAO DEVERÁ SER "efetua_calculo"

n1 = float(input("1o valor: "))
oper = input("operando | + | - | * | / |: ")
n2 = float(input("2o valor: "))  

def efetua_calculo(n1, n2, oper = '+'):
    
    match oper:
        case '+': 
            print(n1 + n2)
        case '-':
            print(n1 - n2)
        case '*':
            print(n1 * n2)
        case '/':
            if (n2 == 0):
                print("Não é possível dividir por zero")
            else:
                print(n1 / n2)
        case _: 
            print("Operacao Invalida")
      
efetua_calculo(n1, n2, oper)