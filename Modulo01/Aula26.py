from time import sleep

valor = "Sim"

while valor.capitalize() == "Sim":
        valor = int(input("Digite o número de nomes que deseja inserir na lista: "))

        nomes = []

        for i in range(1, valor+1):
            nome = input(f"Digite o {i} nome: ")
            nomes.append(nome)

        for i in range(5):
            print("*") 
            sleep(1)
    
        print("Sua lista de nomes é:")

        for nome in nomes:
            print(nome)

        valor = input("Voce deseja continuar no sistema? Sim ou Não ")
        
for i in range(5):
    print("*") 
    sleep(1)
print("Você saiu do sistema")