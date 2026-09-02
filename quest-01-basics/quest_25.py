###Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.###
#entrada = input().split     #solução que encontrei na internet 
a = float(input())
b = float(input())
c = float(input())
triangulo = (c*a)/2
circulo = (c**2)*3.14159
trapezio =  ((a+b)*c)/2
quadrado = b**2
retangulo = a*b


print(f"TRIANGULO: {triangulo:0.3f}")
print(f"CIRCULO: {circulo:0.3f}")
print(f"TRAPEZIO: {trapezio:0.3f}")
print(f"QUADRADO: {quadrado:0.3f}")
print(f"RETANGULO: {retangulo:0.3f}")