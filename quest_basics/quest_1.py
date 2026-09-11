def Cadastro():
    print("Bem-vindo Usuario!")
    nome = (input("Digite seu nome: "))
    cpf = (input("Digite seu CPF: "))
    numero = (input("Digite seu numero de telefone: "))
    print("cadastro realizado com sucesso!",nome,cpf,numero)

print("Bem-vindo ao sistema de cadastro!")
print("se vc quer continuar digite 1, se não digite 0 ")
resposta = int(input("Digite sua resposta: "))
if resposta == 1:
    Cadastro()
else:    
    print("Obrigado por usar nosso sistema de cadastro, volte sempre!")