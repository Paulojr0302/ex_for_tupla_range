import os
os.system('cls')

lista = []
contador = 0
cont = 1

print('Digite 5 numeros inteiros:  ')

while contador < 5:
    numero = int(input(f'Digite o {cont}º numero: '))
    lista.append(numero)
    cont +=1
    contador+=1

lista_max = max(lista)
print(f'O maior numero da lista {lista} é {lista_max}')

