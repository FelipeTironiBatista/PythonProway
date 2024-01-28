nome = input("Digite seu Nome >> ")
idade = int(input("Digite sua idade >> "))

if(idade == 18):
    print(f"Você {nome} tem exatamente 18 anos de idade")

elif(idade > 18):
    print(f"Você {nome} é maior de idade")

else:
    print(f"Você {nome} é menor de idade")