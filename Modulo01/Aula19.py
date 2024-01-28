nivel = int(input("Digite o seu nivel de experiencia profissional entre (1 ate 10) >> "))

if(nivel < 1):
    mensagem = "Você nunca trabalhou na vida"

if(nivel >=1 < 3):
    mensagem = "Você foi apenas jovem aprendiz"

if(nivel >=3 < 6):
    mensagem = "Você já trabalha há alguns anos"
    
if(nivel >=6  <= 9):
    mensagem = "Você é um bom Profissional"
    
if(nivel > 9):
    mensagem = 'Você já está perto de se aposentar'

print(mensagem)
    