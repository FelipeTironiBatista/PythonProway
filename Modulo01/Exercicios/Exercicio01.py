#Vamos explorar a ideia de um carro e criar variáveis correspondentes a diferentes atributos, 
#como marca, cor, potência e valor.
#Para isso, cada variável será preenchida através de uma interação com o usuário, onde 
#solicitaremos os dados necessários.
#Ao finalizar a coleta de informações, iremos exibir os dados utilizando interpolação de 
#string para destacar os valores respectivos de cada atributo.

marca = input("Informe a marca do veículo: ")
modelo = input("Informe o modelo do veículo: ")
cor = input("Informe a cor do veículo: ")
potencia = input("Informe a potência do veículos: ")
valor = int(input ("Informe o valor do veículos: "))

print(f"Os dados informados foram: \nMarca: {marca} \nModelo: {modelo} \nCor: {cor} \nPotência: {potencia} cv \nValor: R$ {valor}")