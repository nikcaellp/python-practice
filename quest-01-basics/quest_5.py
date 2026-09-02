#codigo que calcula a raiz quadrada através da biblioteca MATH, ao final arredonda para mais
import math
numb = int(input("Digite um numero: "))
raiz = math.sqrt(numb)

print(f"a raiz desse numero é: {math.ceil(raiz)}")