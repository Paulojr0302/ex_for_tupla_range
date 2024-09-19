import os
os.system('cls')

nomes = []
saltos = []

nome = input('Nome do atleta: ')
while nome != '':
    nomes.append(nome)

    cont = 1
    contador = 0
    saltos_atleta = []

    while contador < 5:
        salto = float(input(f'Distância do {cont}º salto: '))
        saltos_atleta.append(salto) 
        os.system('cls')   
        cont += 1
        contador += 1

    saltos.append(saltos_atleta)

    nome = input('Nome do próximo atleta: ')
    os.system('cls')

for i in range(len(nomes)):
    nome_atleta = nomes[i]
    saltos_atleta = saltos[i]

    maior_salto = max(saltos_atleta)
    menor_salto = min(saltos_atleta)

    saltos_restantes = sorted(saltos_atleta)[1:4] 
    media_saltos = sum(saltos_restantes) / len(saltos_restantes)

    print(f"\nAtleta: {nome_atleta}")
    print(f"Saltos: {saltos_atleta}")
    print(f"Melhor salto: {maior_salto} m")
    print(f"Pior salto: {menor_salto} m")
    print(f"Média dos outros 3 saltos: {media_saltos:.2f} m")