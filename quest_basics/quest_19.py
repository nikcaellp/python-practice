velo = int(input("Digite quanto Kms da viagem de carro: "))

preco = velo*0.50 if velo<=200 else velo*0.45   #Maneira Compacta de Utilizar condicionais
print(f"Valor da sua viagem é: R${preco}")  


if velo <= 200:
    velo = float(velo *0.5)

    print(f"O valor da sua viagem ficara: R${velo} ")
else:
    velo = float(velo *0.45)
    print(f"O valor da sua viagem longa ficara: R${velo} ")


