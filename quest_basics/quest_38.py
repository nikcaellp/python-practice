valor = float(input("Qual o valor da casa: "))
sala = float(input("Qual o salário: "))
anos = int(input("quantos anos pra pagar: "))
anos*=12
percento = (sala*30)/100
prestacao = valor/anos

print(f"Para pagar uma casa de :R${valor} em {int(anos/12)} anos\nO valor da prestação :{prestacao:0.2f},\n30% do salario: {percento}", end="")
if prestacao >percento:
    print("Emprestimo \033[1;31m Negado\033[m")
    print(f"30% ={percento}\nPrestacao é {prestacao}")
    
elif prestacao == percento:
    print("Emprestimo aprovado por pouco")

else:
    print("\033[1;32m APROVADO\033[m")