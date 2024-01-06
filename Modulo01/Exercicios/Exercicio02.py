#Criando variáveis para descrever um animal.
#Crie variáveis correspondentes a:
#Tipo de animal, Cor, Idade, Som que o animal faz
#Cada variável deve ser preenchida com dados fornecidos pelo usuário, 
#através de interações específicas. 
#Depois de coletar as informações, utilize a Mascara de substituicao para exibir os dados 
#de forma clara e organizada.

tipo = input("Informe o tipo do animal: ")
cor = input("Informe a cor do animal: ")
idade = input("Informe a idade do animal: ")
som = input("Informe o som que o animal produz: ")

print("O animal descrito é um(a) {} cuja cor é {}, com idade aproximada de {} anos e que se comunica através de {}." .format(tipo, cor, idade, som))

