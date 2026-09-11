#Codigo que calcula o gasto de tinta em uma parede, utilizando Largura x Altura

largura = float(input("Digite a largura da parede em Mts: "))
altura = float(input("Digite a altura da parede em Mts: "))
 #cada litro de tinta pinta 2m² 

area = largura * altura

print(f"A area da parede é de {'\033[33m'}{area:0.1f}m²{'\033[m'}")
total = area/2

print(f"o total de tinta pra pintar a parede é {'\033[1;36m'}{total}lt{'\033[m'}")

