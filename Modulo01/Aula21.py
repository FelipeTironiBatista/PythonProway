numero = int(input("Digite o numero da Tabuada que voce deseja saber "))

for i in range(1, 11):
    print("{} X {} = {}".format(numero, i, numero*i))