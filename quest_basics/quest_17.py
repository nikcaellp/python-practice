velo = int(input("Digite a velocidade do carro em Kms: "))

if velo >80:
    velo = (velo-80)*7

    print(f"Você foi multado {"\n\033[1;31m"}A multa foi: R${velo}{"\033[m"} ")             #\033[31m = cor vermelha#
else:
    print("\033[1;32mVocê pode seguir, está sem multas ")                           #\033[32m = cor Verde#