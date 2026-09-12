preco = float(input("Digite um valor: "))

print("opcao 1- avista")
print("opcao 2- avista no cartao")
print("opcao 3- 2X no cartao")
print("opcao 4- 3x no cartao ou mais")
opc = int(input("Digite como vc vai pagar: "))

if opc ==1:
    print(f"Valor com %10 de desconto: RS${(preco-(preco*10)/100):.2f}")
elif opc ==2:
    print(f"Valor com %5 de desconto: RS${(preco-(preco*5)/100):.2f}")
elif opc ==3:
    print(f"Valor normal: RS${preco}")
elif opc ==4:
    print(f"Valor com %20 de juros: RS${(preco+(preco*20)/100):.2f}")