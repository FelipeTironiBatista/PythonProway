from time import sleep

situacao = "Reprovado"
while situacao == "Reprovado":
    #Bloco 1
    nome = input("Digite Seu Nome >> ")
    sobrenome = input("Digite Seu Sobrenome >> ")
    idade = int(input("Digite Sua Idade >> "))
    notas=[]
    #Bloco 2
    for i in range(1,5):
        nota = float(input(f"Digite sua {i} Nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    #Bloco 3
    if(media < 7.0):
        situacao = "Reprovado"
    
    elif(media >= 7.0):
        situacao = "Aprovado"
        for i in range(10):
            print("*")
            sleep(1)
        print("Parabens voce foi aprovado no curso de python")
    #Bloco 4
    Aluno = {
                    "Nome": nome,
                    "SobreNome": sobrenome,
                    "Idade": idade,
                    "Notas": notas,
                    "Media": media,
                    "Situacao": situacao
            }
    #Bloco 5
    var= input("Deseja saber os dados completos do aluno? \nsim\nnao\n >> ")
    if var.capitalize() == "Sim":
        print( f'''
    {Aluno['Nome']}
    {Aluno["SobreNome"]}
    {Aluno["Idade"]}
    {Aluno["Notas"]}
    {Aluno["Media"]}
    {Aluno["Situacao"]}
    ''')