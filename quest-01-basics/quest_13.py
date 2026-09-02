nome = input("Digite o nome de uma cidade: ")

resposta = nome.upper().find("SANTO")
if resposta == 0 :
    print("Essa cidade tem santo no começo!!!")
else: 
    print("Essa cidade não tem santo no começo ")