sal = float(input("Digite o salário:"))

if sal <=1250:
    novo = (sal//100)*15
    print(f"Aumento de 15%\nNovo salario de : R${(novo+sal):.1f}")
else:
    novo = (sal/100)*10
    print(f"Aumento de 10%\nNovo salario de : R${(novo+sal):.1f}")