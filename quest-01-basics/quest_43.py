from datetime import date

ano = int(input("Digite seu ano de nascimeto: "))
ano_atual = date.today().year
idade = ano_atual-ano

if idade <=9:
    print("Sua categoria é MIRIM")

elif idade>10 and idade<=14:
    print("Sua categoria é INFANTIL")

elif idade>15 and idade<=19:
    print("Sua categoria é JUNIOR")

elif idade==20:
    print("Sua categoria é SÊNIOR")
else:
    print("MASTER")