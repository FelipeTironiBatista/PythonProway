#O objetivo deste programa é realizar o sorteio de 1 nome de uma lista de 6 nomes.

import random

#Aqui eu peço ao usuário para informar os nomes que serão utilizados no sorteio.
Nome1 = input("Digite o 1o nome: ")
Nome2 = input("Digite o 2o nome: ")
Nome3 = input("Digite o 3o nome: ")
Nome4 = input("Digite o 4o nome: ")
Nome5 = input("Digite o 5o nome: ")
Nome6 = input("Digite o 6o nome: ")

#Aqui eu monto a lista de nomes, tendo por base os nomes informados pelo usuário nas variáveis Nome*
listaNomes = [Nome1, Nome2, Nome3, Nome4, Nome5, Nome6]

#Aqui eu executo o sorteio. 
sorteio = random.choice(listaNomes)

#Aqui eu apresento o nome que foi sorteado.
print(f"O nome {sorteio} foi o sorteado!")


