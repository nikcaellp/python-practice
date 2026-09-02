from datetime import date
ano = int(input("Digite Um ano: Coloque 0 para o ano atual: "))

if ano ==0:
    ano = date.today().year

if ano %4==0 and ano%100 !=0 or ano %400==0:
    print("ano Bissexto 1 if")

else:
    print("não é bissexto")