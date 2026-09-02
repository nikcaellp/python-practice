from random import randint,random,shuffle
num = int(input("Digite quanto alunos são:"))
nomes =[]
for i in range(num):
    name = input(f"digite o nome do {num} aluno: ")
    nomes.append(name)

num = randint(0,num)
print(f"O aluno escolhido é: {nomes[num]} ")
shuffle(nomes)              #SHUFFLE serve basicamente com um embaralhador de possições em uma lista#
print(f" A ordem ficou assim: {nomes}")
