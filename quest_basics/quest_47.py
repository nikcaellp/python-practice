from time import sleep
from random import randint
jogo = ("PEDRA","PAPEL","TESOURA")
print("\033c",end="")
print("Vamos Jogar Jokenpô!!!\n")
opc =1
numb_J=0
numb_C=0
numb_D=0

while opc!=0:
    i= randint(0,2)
    pc = jogo[i]
    chute = input("DIGITE SUA ESCOLHA: ").strip().upper()
    
    print("\033c",end="")
    print("JO")
    sleep(1)
    print("KÊN")
    sleep(1)
    print("PO")
    sleep(1)
    print("\033c",end="")

    print("="*25)
    print(f"O computador: {pc}".center(25,"-"))
    print(f"O jogador: {chute.upper()}".center(25,"-"))
    print("="*25)

    if chute==pc==jogo[i]==chute:
        print("\033[34mEMPATE!!!\033[m ")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_D+=1

    elif chute ==jogo[0] and pc==jogo[2]:
        print(f"{"\033[32m"}Jogador ganhou!!!!!{"\033[m"}")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_J+=1

    elif chute==jogo[0] and pc==jogo[1]:
        print(f"{"\033[31m"}Computador ganhou!!!!{"\033[m"}\n")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_C+=1

    elif chute ==jogo[1] and pc==jogo[2]:
        print(f"{"\033[31m"}Computador ganhou!!!!{"\033[m"}\n")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_C+=1

    elif chute==jogo[1] and pc==jogo[0]:
        print(f"{"\033[32m"}Jogador ganhou!!!!!{"\033[m"}")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_J+=1

    elif chute ==jogo[2] and pc==jogo[0]:
        print(f"{"\033[31m"}Computador ganhou!!!!{"\033[m"}\n")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_C+=1

    elif chute==jogo[2] and pc==jogo[1]:
        print(f"{"\033[32m"}Jogador ganhou!!!!!{"\033[m"}")
        opc= int(input("vc quer tentar novamente?\nDigite 1-sim, 0-Não: "))
        numb_J+=1

    else:
         print("\033c",end="")
         print("ERROR,NÃO VALIDO")
         continue

print("\033c",end="")
print("""PLACAR DE VITORIAS
Numeros do Jogador= {}
Numeros do Computador= {}
Numeros de Empates= {}""".format(numb_J,numb_C,numb_D))
print("OBRIGADO POR JOGAR!!!")