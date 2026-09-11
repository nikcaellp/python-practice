nome = str(input("Digite seu nome: ")).strip().upper()

separado = nome.split()

print(f"O seu Primeiro nome é {separado[0]}, e o Ultimo nome é : {separado[-1]}")