#Exercício: Tabuada Personalizada
#Neste exercício, o objetivo é criar um programa Python que 
#gere a tabuada personalizada de um número escolhido pelo usuário. 
#Vamos realizar esse exercício utilizando instruções simples em Python.

#Obtenção do Número:
#Inicie solicitando ao usuário que forneça um número para o qual deseja gerar a tabuada. 
#Utilize a função input para receber a entrada do usuário e converta-a para um número inteiro.

#Geração da Tabuada sem Loop:
#Crie um bloco print.
#Abra uma string e adicione três chaves vazias dentro da string.
#Após a string, adicione a função .format(), que representa a máscara de substituição.
#Dentro da função, coloque a variável que pega os dados digitados pelo usuário.
#Em seguida, coloque um número fixo representando o cálculo da tabuada.
#Finalmente, adicione a variável multiplicada pelo número fixo.
#Lembre-se de que a tabuada vai de 1 a 10, então o número fixo representa cada número individual 
#nesse intervalo.

#Finalização do Programa:
#Ao finalizar a exibição da tabuada, o programa deve encerrar.
#Este exercício visa praticar a manipulação de strings e a exibição de 
#informações de forma sequencial sem o uso explícito de um loop. 
#Ao seguir essas instruções, você poderá criar um programa simples e eficaz 
#para gerar uma tabuada personalizada.

var = "="*54

print(var)

fator1 = int(input("Informe o número para o qual o tabuada será gerada: "))

print("{} x {} = {}" .format(fator1 , 1 ,fator1*1))
print("{} x {} = {}" .format(fator1 , 2 ,fator1*2))
print("{} x {} = {}" .format(fator1 , 3 ,fator1*3))
print("{} x {} = {}" .format(fator1 , 4 ,fator1*4))
print("{} x {} = {}" .format(fator1 , 5 ,fator1*5))
print("{} x {} = {}" .format(fator1 , 6 ,fator1*6))
print("{} x {} = {}" .format(fator1 , 7 ,fator1*7))
print("{} x {} = {}" .format(fator1 , 8 ,fator1*8))
print("{} x {} = {}" .format(fator1 , 9 ,fator1*9))
print("{} x {} = {}" .format(fator1 , 10 ,fator1*10))

print(var)