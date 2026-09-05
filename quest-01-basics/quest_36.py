# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes,
# mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada
# Leia três valores de ponto flutuante (double) A, B e C.

# Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
# Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.
# Imprima sempre o final de linha após cada mensagem.
a,b,c= map(float,input().split())
if a ==0:
    print("Impossivel de calcular")
else:
    delta = (b**2)-(4*a*c)
    print(delta)
    if delta >=0:
        x1 = ((-b) + (delta **(1/2)))/(2*a)
        x2 = ((-b) - (delta **(1/2)))/(2*a)
        print(f"R1 = {x1:.5f}")
        print(f"R1 = {x2:.5f}")
    else:
        print("Impossivel de calcular")