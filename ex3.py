import os
os.system('cls')
multiplicacao_total = 1
total = 0

print('Digite cinco numeros para a lista:  ')
lista = []

while total < 5:
    numero = int(input('Insira um numero: '))
    lista.append(numero)
    total += 1

soma_lista = sum(lista)

for numero in lista:
    multiplicacao_total *= numero

print(f'lista: {lista}')
print(f'Soma total da lista: {soma_lista}')
print(f'Multiplicação total da lista: {multiplicacao_total}')

    





