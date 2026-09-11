nome = str(input("Digite seu nome completo: ")).strip()     #Função STRIP serve para retirar espaços inuteis em começos de Strings#

print(f"Maisculo:{nome.upper()}")       #Função UPPER serve para colocar todas as letras em Maisculas de uma String#
print(f"Minusculo:{nome.lower()}")        #Função LOWER serve para colocar todas as letras em Minusculas de uma String#
print(f"quantas letras tem ao todo:{len(nome.replace(" ",""))}")        #Função REPLACE serve para TROCAR caracteres por outros em Strings#
print(f"quantas letras tem ao todo:{len(nome)-nome.count(" ")}") ##correção do video do guanabara
print(f"identizado:{nome.title()}")
print(f"o primeiro nome tem esse total de letras: {nome.find(" ")}")       #Função que Serve para localizar Caracteres em uma String#
nome =nome.split()      #Função que Serve para DIVIDIR uma Lista em varias Listas#

print("O primeiro nome tem esse total de letras: {}".format(len(nome[0])))  #Função que LER o tamanho de uma String#

