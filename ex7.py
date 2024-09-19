import os
os.system('cls')

impares = []

lista = list(range(1, 51))

for i in lista:
    if(i%2==1):
        impares.append(i)
    
print(impares)