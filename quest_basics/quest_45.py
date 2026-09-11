altura = float(input("Digite sua altura em cm: "))
peso = float(input("Digite seu peso em kgs: "))

imc = peso/(altura**2)
if imc<18.5:
    print("Abaixo do peso")

elif imc>=18.5 or imc<25:
    print("peso ideal")
    
elif imc>=25 or imc<30:
    print("peso ideal")

elif imc>=30 or imc<40:
    print("peso ideal")

else:
    print("Obesidade morbida")