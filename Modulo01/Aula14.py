import random

nome1 = input("Digite Seu Nome >> ")
nome2 = input("Digite Seu Nome >> ")
nome3 = input("Digite Seu Nome >> ")
nome4 = input("Digite Seu Nome >> ")

ListaNome = [nome1, nome2, nome3, nome4]
print(ListaNome)

sorteio = random.choice(ListaNome)

print(sorteio)