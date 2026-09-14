numb = []
s =0
for i in range(1,6+1):
    n=int(input("Digite um valor: "))
    numb.append(n)
    if numb[i-1]%2==0:
        s+=numb[i-1]
print(s)