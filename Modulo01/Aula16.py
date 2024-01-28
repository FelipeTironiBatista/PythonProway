a = "="*20 #Polimorfismo

print(a,"Primeiro Funcionario",a)

nome1 = str(input("Digite seu nome >> "))
idade1 = int(input("Digite sua idade >> "))
salario1 = float(input("Digite Seu Salario >> ")) 

print(a,"Segundo Funcionario",a)

nome2 = str(input("Digite seu nome >> "))
idade2 = int(input("Digite sua idade >> "))
salario2 = float(input("Digite Seu Salario >> ")) 

print(a,"Terceiro Funcionario",a)

nome3 = str(input("Digite seu nome >> "))
idade3 = int(input("Digite sua idade >> "))
salario3 = float(input("Digite Seu Salario >> ")) 

print(a,"Quarto Funcionario",a)

nome4 = str(input("Digite seu nome >> "))
idade4 = int(input("Digite sua idade >> "))
salario4 = float(input("Digite Seu Salario >> ")) 

Funcionario1 = {"Nome": nome1, "Idade": idade1, "Salario": salario1}
Funcionario2 = {"Nome": nome2, "Idade": idade2, "Salario": salario2}
Funcionario3 = {"Nome": nome3, "Idade": idade3, "Salario": salario3}
Funcionario4 = {"Nome": nome4, "Idade": idade4, "Salario": salario4}

listaFuncionarios = [Funcionario1, Funcionario2, Funcionario3, Funcionario4]

print(a,"Primeiro Funcionario",a)
print(listaFuncionarios[0])

print(a,"Primeiro Funcionario",a)
print(listaFuncionarios[1])

print(a,"Primeiro Funcionario",a)
print(listaFuncionarios[2])

print(a,"Primeiro Funcionario",a)
print(listaFuncionarios[3])


