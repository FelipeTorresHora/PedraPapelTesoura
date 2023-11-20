from func import *

print("############ JOGO: Pedra, Papel, Tesoura ############")
print("Digite uma das opções:\nPedra\nPapel\nTesoura")
while True:
    ope = input("Digite o numero da função que você quer acessar: ")
    if ope == "Pedra":
        pedra("pedra")
        break
    elif ope == "Papel":
        papel("papel")  
        break
    elif ope == "Tesoura":
        tesoura("tesoura") 
        break
    else:
        print("Operação Inválida")