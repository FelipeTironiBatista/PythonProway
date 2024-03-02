#Elabore um algoritmo que peça para o usuario infomar o valor inicial e o valor final
#Deverá retornar a quantidade de valores pares existentes nesse intervalo
#Retornar a média aritmética dos valores impares do intervalo

x = 2 % 2 == 0
print(x)

vini = int(input("Informe o valor inicial: "))
vfim = int(input("Informe o valor final: "))
pares = 0
media = 0
soma_impares = 0
total_impares = 0

while (vini <= vfim):
    if (vini % 2 == 0):
        pares += 1
    else:
        total_impares += 1
        soma_impares = soma_impares + vini
    vini += 1
    
print(pares)
print(soma_impares / total_impares)
        
        