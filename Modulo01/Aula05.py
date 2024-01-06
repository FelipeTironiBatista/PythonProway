#Criando formas constantes de acesso a dados inconstantes
nome = input("Digite seu nome ")
sobrenome = input("Digite seu sobrenome ")
idade = int(input("Digite sua idade "))

#interpolação de string
#formato de impressão que permite valores em uma unica string
# f = format
# \n = quebra a linha da impressao. O texto apos a quebra deve ficar "colado" ao \n para evitar a adição indevida de um espaço.
print(f"O nome é {nome} \nO sobrenome é {sobrenome} n\A idade é {idade}")