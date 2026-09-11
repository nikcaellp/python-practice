#Codigo que calcula o salario final com aumento de 15%
salario = float(input("Digite o valor do Salario: "))
percent = (salario * 15) /100
result = salario + percent
print(f"SALARIO INICIAL: {salario}\nAUMENTO: {percent}\nVALOR FINAL: {result}")