print("Analisador de triangulo".center(30,"="))

r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))

if r1 <r2 +r3 and r2 <r1 +r3 and r3 <r2 +r1:
    print(f"{"\033[32m"}Forma Triangulo{"\033[m"}")

    if r1==r2 and r2 ==r3:
        print("Tipo: Equilatero")
    elif r1==r2 or r1==r3 or r2==r3:
        print("Tipo: Isosceles")
    elif r1!=r2 and r2!=r3:
        print("Tipo: Escaleno")

else:
    print("\033[0;30;41m Não forma Triangulo\033[m")