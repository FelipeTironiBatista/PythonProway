#Elabore um algoritmo em que o usuario ira digitar dos valores numericos e apos isso deve pedir
#a operacao aritmetica desejada [adicao | subtracao | multiplicao | divisao]

from time import sleep

print("+------------------------+ \n|Calculadora             | \n+------------------------+")

valor1 = int(input("Informe o 1o valor: "))
valor2 = int(input("Informe o 2o valor: "))
print("+------------------------+")
print("Informe a operacao desejada, sendo:\n1-Adicao \n2-Subtracao \n3-Multiplicacao \n4-Divisao")
oper = int(input("Informe a operacao desejada: "))
print("+------------------------+")

match oper:
    case 1:
#if oper == 1:
        print("Resultado: ", int(valor1 + valor2))
    case 2:
#elif oper == 2:
        print("Resultado: ", int(valor1 - valor2))
    case 3:
#elif oper == 3:
        print("Resultado: ", int(valor1 * valor2))
    case 4:
#elif oper == 4:
        if (valor2 == 0):
            print("Impossível dividir por zero")
        else:
            print("Resultado: ", int(valor1 / valor2))
    case _: #Neste contexto é possível utilizar o Default
#else
        print("Opcao invalida")





