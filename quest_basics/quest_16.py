from random import randint
from time import sleep
numb = int(input("Digite qualquer numeror entre 1 e 10:"))

s = randint(1,10)

while s != numb:
    if numb<s:
        print("PENSANDO...")
        sleep(2)
        print("Chute muito baixo")
     
        numb = int(input("tente novamente qualquer numeror entre 1 e 10:"))
    else:
        print("PENSANDO...")
        sleep(2)
        print("chute muito alto")

        numb = int(input("tente novamente numeror entre 1 e 10:"))