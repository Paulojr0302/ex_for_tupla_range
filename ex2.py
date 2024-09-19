import os
os.system('cls')

print('Digite dois numeros para a lista:  ')
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))

lista = list(range(num1 + 1,num2))

print(lista)
