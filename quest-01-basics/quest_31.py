#Desafio 1018 beecrowd
#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
#As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

#Entrada
#O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

#Saída
#Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. 
#Não esqueça de imprimir o fim de linha após cada linha,
#caso contrário seu programa apresentará a mensagem: “Presentation Error”.
    #Primeira solução
numb = int(input("Digite um numero: "))
print(numb)
valor = [100,50, 20,10,5,2,1]
for i in range(len(valor)):
    result = numb //valor[i]
    print(f"{result} nota(s) de R$ {valor[i]},00",end="\n")
    numb = numb - (result*valor[i])

        #Solução da Internet
# print(f"{numb//100} nota(s) de R$ 100,00")
# numb %= 100
# print(f"{numb//50} nota(s) de R$ 50,00")
# numb %= 50
# print(f"{numb//20} nota(s) de R$ 20,00")
# numb %= 20
# print(f"{numb//10} nota(s) de R$ 10,00")
# numb %= 10
# print(f"{numb//5} nota(s) de R$ 5,00")
# numb %= 5
# print(f"{numb//2} nota(s) de R$ 2,00")
# numb %= 2
# print(f"{numb//1} nota(s) de R$ 1,00")
# numb %= 1
