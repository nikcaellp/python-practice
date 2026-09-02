print("-"*30)
print("Analisador de triangulo".center(30,"="))
print("-"*30)

r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))
if r1 <r2 +r3 and r2 <r1 +r3 and r3 <r2 +r1:
    print("Forma Triangulo")
else:
    print("\033[0;30;41m Não forma Triangulo")