# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
# As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.
quant = float(input("Digite um numero: ")+.001)
quant = str(quant).replace(".","\n").split()
numb= float(quant[0])
numb_m = float(quant[1])/100

real =0
print("NOTAS:")
valor = [10000,5000, 2000,1000,500,200]
for i in range(len(valor)):
    result = numb //valor[i]
    print(f"{int(result)} nota(s) de R$ {valor[i]}.00",end="\n")
    numb -= (result*valor[i])
    if 1 == numb//1:
        real =1.0

numb_m+=real

print("MOEDAS:")
valorm = [100, 50, 25, 10, 5,1]
for i in range(len(valorm)):
    result = numb_m //valorm[i]
    print(f"{int(result)} moeda(s) de R$ {valorm[i]:.2f}",end="\n")
    numb_m -= (result*valorm[i])


# quant = float(input("Digite um numero: "))
# total_centavos = int(quant * 100 + 0.001)
# print("NOTAS:")
# print(f"{int(quant//100)} nota(s) de R$ 100.00",end="\n")
# quant %= 100
# print(f"{int(quant//50)} nota(s) de R$ 50.00",end="\n")
# quant %= 50
# print(f"{int(quant//20)} nota(s) de R$ 20.00",end="\n")
# quant %= 20
# print(f"{int(quant//10)} nota(s) de R$ 10.00",end="\n")
# quant %= 10
# print(f"{int(quant//5)} nota(s) de R$ 5.00",end="\n")
# quant %= 5
# print(f"{int(quant//2)} nota(s) de R$ 2.00",end="\n")
# quant %= 2
# print("MOEDAS:")
# print(f"{int(total_centavos//1)} moeda(s) de R$ 1.00",end="\n")
# total_centavos %= 1
# print(f"{int(total_centavos//0.50)} moeda(s) de R$ 0.50",end="\n")
# total_centavos %= .50
# print(f"{int(total_centavos//.25)} moeda(s) de R$ 0.25",end="\n")
# total_centavos %= .25
# print(f"{int(total_centavos//.10)} moeda(s) de R$ 0.10",end="\n")
# total_centavos %= .10
# print(f"{int(total_centavos//0.05)} moeda(s) de R$ 0.05",end="\n")
# total_centavos %= .05
# print(f"{int(total_centavos//0.01)} moeda(s) de R$ 0.01",end="\n")