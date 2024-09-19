import os
os.system('cls')

nomes = []
notas = []

nome = input('Nome do atleta: ')
while nome != '':
    nomes.append(nome)

    cont = 1
    contador = 0
    notas_atleta = []

    while contador < 7:
        nota = float(input(f'nota do {cont}º jurado: '))
        notas_atleta.append(nota) 
        os.system('cls')   
        cont += 1
        contador += 1

    notas.append(notas_atleta)

    nome = input('Nome do próximo atleta: ')
    os.system('cls')

for i in range(len(nomes)):
    nome_atleta = nomes[i]
    notas_atleta = notas[i]

    maior_nota = max(notas_atleta)
    menor_nota = min(notas_atleta)

    notas_restantes = sorted(notas_atleta)[1:4] 
    media_notas = sum(notas_restantes) / len(notas_restantes)

    print(f"\nAtleta: {nome_atleta}")
    print(f'Notas: {notas[i]}')
    print(f"Melhor nota: {maior_nota} m")
    print(f"Pior nota: {menor_nota} m")
    print(f"Média: {media_notas:.2f} m")