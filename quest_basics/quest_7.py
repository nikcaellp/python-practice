from math import sqrt
oposto = float(input("Digite o cumprimento do cateto oposto: "))
adjacente = float(input("Digite o cumprimento do cateto adjacente: "))

oposto = oposto**2
adjacente = adjacente**2

print(f"O valor da Hipotenusa é:{sqrt(oposto + adjacente):0.1f}")
