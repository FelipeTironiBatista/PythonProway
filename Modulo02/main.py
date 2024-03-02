from revendedora import Carro, Moto
import os, time

def executaEAguarda(metodo, tempo):
    print(metodo)
    time.sleep(tempo)

def defineTempoEspera(tempo, exibeMsg = False):
    global TEMPO_ESPERA
    TEMPO_ESPERA = tempo
    if(exibeMsg):
        print(f"O novo tempo configurado foi de {TEMPO_ESPERA}" + (' segundos.' if TEMPO_ESPERA > 1 else ' segundo.'))

def exibeMenu():
    global TEMPO_ESPERA
    TEMPO_ESPERA = 3
    opcao = 0
    os.system("cls")
    while (opcao != 6):
        print('+-------------------------------------------+')
        print('| Selecione a opção desejada                |')
        print('+-------------------------------------------+')
        print('| 1 - Ligar                  2 - Desligar   |')
        print('| 3 - Acelerar               4 - Reduzir    |')
        print('| 5 - Tempo Espera           6 - Encerrar   |')
        print('+-------------------------------------------+')
        try:
            opcao = int(input("Selecione a operacao desejada:  "))
            match opcao:
                case 1:
                    # print(veiculo.ligar())
                    # time.sleep(TEMPO_ESPERA)
                    executaEAguarda(veiculo.ligar(),TEMPO_ESPERA)
                case 2:
                    # print(veiculo.desligar())
                    # time.sleep(TEMPO_ESPERA)
                    executaEAguarda(veiculo.desligar(),TEMPO_ESPERA)
                case 3:
                    # print(veiculo.acelerar())
                    # time.sleep(TEMPO_ESPERA)
                    executaEAguarda(veiculo.acelerar(),TEMPO_ESPERA)
                case 4:
                    # print(veiculo.reduzir())
                    # time.sleep(TEMPO_ESPERA)
                    executaEAguarda(veiculo.reduzir(),TEMPO_ESPERA)
                case 5:   
                    tempo = int(input("Quantos segundos cada mensagem deve aguardar na tela? "))
                    defineTempoEspera(tempo, True)
                    time.sleep(TEMPO_ESPERA)
                case 6:
                    # print('Obrigado por usar o sistema')
                    executaEAguarda(print('Obrigado por usar o sistema!'),TEMPO_ESPERA)
                case _: 
                    # print('Opcao invalida!')
                    # time.sleep(TEMPO_ESPERA)
                    executaEAguarda(print('Opcao invalida'),TEMPO_ESPERA)
        except ValueError:
            executaEAguarda('Necessario informar um valor numerico', TEMPO_ESPERA)
        except ZeroDivisionError:
            executaEAguarda("Impossivel dividir por zero", TEMPO_ESPERA)
        except Exception: #O exception precisa ficar por ultimo. Dessa forma, e garantido que os demais tratamento serao aplicados. 
            executaEAguarda("Ocorreu um erro ao processar a rotina", TEMPO_ESPERA)
        os.system("cls")

def defineAtributos(ehCarro = True):
    global v_ano
    global v_cor
    v_cor = input('Digite a cor ' + ('do carro:  ' if ehCarro else 'da moto: '))
    v_ano = int(input('Digite o ano ' + ('do carro: ' if ehCarro else 'da moto: ')))
    
def instancia():
    global veiculo #global indica que a variavel declarada aqui pode ser utilizada em todo o programa.
    opcao = int(input('Deseja criar: 1 - Carro | 2 - Moto '))
    if (opcao == 1):
        defineAtributos()
        veiculo = Carro(v_cor, v_ano)
    else:
        defineAtributos(False)
        veiculo = Moto(v_cor, v_ano)
    exibeMenu()

if (__name__ == '__main__'):
    instancia()