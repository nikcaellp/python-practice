nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1+nota_2)/2

if media<5.0:
    print(f"{"\33[31:m"}REPROVADO{"\33[m"}")
    
elif media>=5.0 and media<=6.9:
    print(f"{"\33[35:m"}RECUPERAÇÂO{"\33[m"}")

elif media >7.0:
    print(f"{"\33[32:m"}APROVADO{"\33[m"}")