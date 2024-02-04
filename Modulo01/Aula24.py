from time import sleep

valor = int(input("Digite o número de nomes que deseja inserir na lista: "))

nomes = []

for i in range(1, valor+1):
    nome = input(f"Digite o {i} nome: ")
    nomes.append(nome)

for i in range(10):
    print("*") 
    sleep(1)
    
print("Sua lista de nomes é:")

for nome in nomes:
    print(nome)

    
