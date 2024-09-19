import os
os.system('cls')

numero = int(input('Digite um numero:  '))
fatoracao = 1

for i in range(1, numero + 1):
    fatoracao *= i

print(f'O fatorial de {numero} é {fatoracao}')
    

