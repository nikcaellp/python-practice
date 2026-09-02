#Codigo que calcula o valor final com desconto de 5%
price = float(input("Digite o valor do produto: "))
percent = (price * 5) /100
result = price - percent
print(f"VALOR INICIAL: {price}\nDESCONTO: {percent}\nVALOR FINAL: {result}")