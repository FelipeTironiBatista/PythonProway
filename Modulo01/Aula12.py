print("Seja bem-vindo a escola de programação Proway")
nome = str(input("Digite o nome do aluno "))
n1 = float(input("Digite a primeira nota >> "))
n2 = float(input("Digite a segunda nota >> "))

#Polimorfismo
var = "="*20

#Procedência aritmética = utilizar parenteses para indicar ao programa a prioridade de execução das operações aritméticas. 
nota = (n1 + n2) / 2


print(var, "MENU DE NOTAS", var)
#Interpolação
print(f"A primeira nota digitada pelo usuário {nome}\né {n1}\n e a segunda nota é {n2}\ne a media é {nota}")



