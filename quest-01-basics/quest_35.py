#beecrowd 1035
# Leia 4 valores inteiros A, B, C e D. A seguir,
#  se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D,
#  ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

# Entrada
# Quatro números inteiros A, B, C e D.

# Saída
# Mostre a respectiva mensagem após a validação dos valores.

a,b,c,d = map(int,input().split())

soma1= c+d
soma2=a+b

if (b>c) and (d>a) and (soma1>soma2)and  (c>=0) and(d>=0)and a%2==0:
   print("Valores aceitos")                                     
else:
    print("Valores nao aceitos")