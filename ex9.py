import os
os.system('cls')

numeros = []
impares = []
pares = []
contador = 0
cont = 1

print('Digite 10 numeros inteiros:  ')

while contador < 10:
    num = int(input(f'Digite o {cont}º número:  '))
    contador += 1
    cont += 1
    numeros.append(num)
    os.system('cls')

for i in numeros:
    if i %2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Imares {impares}')
print(f'Pares {pares}')


    