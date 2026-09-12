altura = float(input("Digite sua altura em cm: "))
peso = float(input("Digite seu peso em kgs: "))
imc = peso/(altura**2)
print(f"Seu IMC é : {imc:0.1f}")
if imc<18.5:
    print("\033[31mAbaixo do peso \033[m")

elif imc<=25:
    print("\033[32mPeso ideal\033[m")
    
elif imc<=30:
    print("\033[33mSobrepeso \033[m")

elif imc<=40:
    print("Obesidade")

else:
    print("Obesidade morbida")