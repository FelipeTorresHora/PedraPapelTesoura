import random 
escolhas = ["pedra","papel","tesoura"]
def pedra(escolha_usuario):
    escolha_automatica = random.choice(escolhas)
    if escolha_automatica == "tesoura":
        print(f"O computador escolheu {escolha_automatica}. Você ganhou!")    
    elif escolha_automatica == "pedra":
        print(f"O computador escolheu {escolha_automatica}. Jogue novamente!")
    elif escolha_automatica == "papel":
        print(f"O computador escolheu {escolha_automatica}.Você perdeu!")
    else: 
        print("Operação inválida. Tente novamente!")

def tesoura(escolha_usuario):
    escolha_automatica = random.choice(escolhas)
    if escolha_automatica == "papel":
        print(f"O computador escolheu {escolha_automatica}.Você ganhou!")
    elif escolha_automatica == "tesoura":
        print(f"O computador escolheu {escolha_automatica}. Jogue novamente!")
    elif escolha_automatica == "pedra":
        print(f"O computador escolheu {escolha_automatica}.Você perdeu!")
    else: 
        print("Operação inválida. Tente novamente!")
        
def papel(escolha_usuario): 
    escolha_automatica = random.choice(escolhas)
    if escolha_automatica == "pedra":
        print(f"O computador escolheu {escolha_automatica}. Você ganhou!")
    elif escolha_automatica == "papel":
        print(f"O computador escolheu {escolha_automatica}. Jogue novamente!")
    elif escolha_automatica == "tesoura":
        print(f"O computador escolheu {escolha_automatica}. Você perdeu!")
    else: 
        print("Operação inválida. Tente novamente!")
