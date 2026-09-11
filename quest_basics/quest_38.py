valor = float(input("Qual o valor da casa: "))
sala = float(input("Qual o salário: "))
anos = int(input("quantos anos pra pagar: "))
anos*=12
percento = (sala*30)/100
prest = valor/anos

print(f"valor da prestação :{prest:0.2f},\n30% do salario: {percento}")
if prest >percento:
    print("Emprestimo \033[1;31m Negado\033[m")
    print(f"30% ={percento}\nprestacao é {prest}")
    
elif prest == percento:
    print("Emprestimo aprovado por pouco")

else:
    print("\033[1;32m APROVADO\033[m")