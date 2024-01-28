from random import choice, shuffle

nome1 = input("Digite Seu Nome >> ")
nome2 = input("Digite Seu Nome >> ")
nome3 = input("Digite Seu Nome >> ")
nome4 = input("Digite Seu Nome >> ")

ListaNome = [nome1, nome2, nome3, nome4]
print(ListaNome)
shuffle(ListaNome)
print(ListaNome)
sorteio = choice(ListaNome)

print(sorteio)