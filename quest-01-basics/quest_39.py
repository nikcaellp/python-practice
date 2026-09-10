
numb = int(input("Digite o numero que vc quer calcular: "))
print("-"*32)
print("|",f"vamos calcular o numero: \33[31:m {numb} \33[m ".center(30,"-"),"|")
print("|","digite 0 pra binario".center(30,"-"),"|")
print("|","digite 1 para octal".center(30,"-"),"|")
print("|","digite 2 para hexadecimal!!!".center(30,"-"),"|")
print("-"*32)
opc = int(input("Digite uma opcao:... "))


resto = []
if opc ==0:
    while numb !=0:
        resto.append(numb%2)
        numb//=2
    print(f"Para expressar esse numero em binario é necessario: {len(resto)} de bits")
    print(resto[::-1])

elif opc ==1:
    while numb !=0:
            resto.append(numb%8)
            numb//=8
    print(f"Para expressar esse numero em octal é necessario: {len(resto)} de bits")
    print(resto[::-1])

elif opc ==2:
    while numb !=0:
        resto.append(numb%16)
        numb//=16
    print(f"Para expressar esse numero em Hexa é necessario: {len(resto)} de bits")
    print(resto[::-1])

else:
    print("VALOR NÃO ACEITADO")