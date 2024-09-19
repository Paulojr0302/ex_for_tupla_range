import os
os.system('cls')
total = 0

lista = []

listaadd = int(input('Digite o primeiro numero da lista: '))
lista.append(listaadd)

while total < 4:
    listaadd = int(input('Digite o proximo numero da lista: '))
    lista.append(listaadd)
    total = total + 1
print(lista)

