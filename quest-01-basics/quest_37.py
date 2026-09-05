#beecrowd 1037
# Você deve fazer um programa 
# que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) 
# este valor se encontra.
# Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

# Entrada
# O arquivo de entrada contém um número com ponto flutuante qualquer.

# Saída
# A saída deve ser uma mensagem conforme exemplo abaixo.
numb = float(input()) *10000
valores = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]
if numb <0 or numb >1000000:
    print("Fora de intervalo")
else:
    if (numb ==0) or (numb<=250000):
        print(f"Intervalo {valores[0]}")

    elif (numb ==250001) or (numb<=500000):
        print(f"Intervalo {valores[1]}")

    elif (numb ==500001) or (numb<=750000):
        print(f"Intervalo {valores[2]}")

    elif (numb ==750001) or (numb<=1000000):
        print(f"Intervalo {valores[3]}")

