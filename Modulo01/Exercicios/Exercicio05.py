#O objetivo deste programa é sortear 1 destino dentre 6 destinos possíveis informados pelo usuário.

import random

#Aqui eu declaro a lista que irá armazenar os destinos.
lista_destinos = []

#Aqui peço para o usuário informar 6 destinos desejados. 
#Cada um dos destinos informados é adicionado a lista.
destino1 = input("Digite o 1o destino: ")
lista_destinos.append(destino1)

destino2 = input("Digite o 2o destino: ")
lista_destinos.append(destino2)

destino3 = input("Digite o 3o destino: ")
lista_destinos.append(destino3)

destino4 = input("Digite o 4o destino: ")
lista_destinos.append(destino4)

destino5 = input("Digite o 5o destino: ")
lista_destinos.append(destino5)

destino6 = input("Digite o 6o destino: ")
lista_destinos.append(destino6)

#Aqui eu aplico a função responsável pela escolha aleatória de um dos destinos contidos na lista.
sorteio = random.choice(lista_destinos)

#Aqui eu apresento o destino que foi escolhido pela função choice. 
print(f"O destino {sorteio} foi o sorteado!")







