print("soma de numeros entre 1 á 500\ne divisivel por 3:")
s =0
for i in range(1,500):
    if i%3==0:
        s+=i    
print(f"A soma dos numeros resulta: {s}")