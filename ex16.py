lista_original = []
lista_pares = []
lista_impares = []
    
while True:
    try:
        numero = int(input("Digite um número: (maior que 11 ou menor que 0 para encerrar: "))
    except ValueError:
        print("Por favor, digite um número inteiro.")
        continue
    
    if numero > 0 or numero > 11:
        break
    
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    
    lista_original.append(numero)

print(f"Lista original: {lista_original}")
print(f"Lista de números pares: {lista_pares}")
print(f"Lista de números ímpares: {lista_impares}")