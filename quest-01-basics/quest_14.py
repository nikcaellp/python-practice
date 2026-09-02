nome = str(input("Digite seu Nome: ")).strip().upper
letter = input("Digite a letra que vc quer saber: ").strip().upper()



print(f"A letra {letter} aparece essa qauntidade de vezes: {nome.count(letter)}")

print(f"A letra {letter} aparece a primeira vez na posição: {nome.find(letter)+1}")

print(f"A letra {letter} aparece a ulteima vez na posição: {nome.rfind(letter)+1}")