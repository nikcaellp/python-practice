from random import randint
pc = ["PEDRA","PAPEL","TESOURA"]

print("Vamos Jogar Jokenpô!!!\n")
opc =1
i= randint(0,2)

while opc!=0:
    chute = input("DIGITE SUA ESCOLHA: ").strip().upper()
    print

    if chute==pc[i]:
        print(f"{"\033[32m"}Voce ganhou!!!!!{"\033[m"}")
        opc =0
    else:
        input(f"{"\033[31m"}Errou, tente novamente:{"\033[m"}\n")
        opc=1