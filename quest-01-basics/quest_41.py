from datetime import date

ano = int(input("Digite seu ano de nascimeto: "))
ano_atual = date.today().year
idade = ano_atual-ano

if idade ==17:
    print("Voce deve se alistar urgente já está em cima da hora")

elif idade>=18:
    print("Voce ja deveria ter se alistado a {} anos".format(idade-18))

elif idade<=16:
    print(f"Voce ainda vai se alistar, falta {18-idade} anos")