from random import randint
num = int(input("Digite quanto alunos são:"))
nomes =[]
for i in range(num):
    name = input("digite o nome do aluno: ")
    nomes.append(name)

num = randint(0,num)

print(f"O aluno sorteado será: {nomes[num]}")
print(nomes)