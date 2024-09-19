import os
os.system('cls')

contador = 1
codigo = 1

alturas = []
pesos = []
codigos = []

while codigo != 0:
    codigo = int(input(f'Digite o codigo do {contador}º aluno:  '))
    if codigo == 0:
        break
    codigos.append(codigo)
    os.system('cls')
    altura = int(input(f'Digite a altura em centimetros do {contador}º aluno: '))
    alturas.append(altura)
    os.system('cls')
    peso = float(input(f'Digite o peso do {contador}º aluno:  '))
    pesos.append(peso)
    os.system('cls')
    contador += 1

peso_max = max(pesos)
peso_min = min(pesos)
altura_max = max(alturas)
altura_min = min(alturas)

index_gordo = pesos.index(peso_max)
index_magro = pesos.index(peso_min)
index_alto = alturas.index(altura_max)
index_baixo = alturas.index(altura_min)

media_altura = sum(alturas) / len(alturas)
media_pesos = sum(pesos) / len(pesos)

print(f'A media total dos pesos é {media_pesos} Kg e da altura é {media_altura} cm')
print(f'Aluno mais magro cod {codigos[index_magro]}, Peso {peso_min} Kg, Altura {alturas[index_magro]} cm')
print(f'Aluno mais gordo cod {codigos[index_gordo]}, Peso {peso_max} Kg, Altura {alturas[index_gordo]} cm')
print(f'Aluno mais alto cod {codigos[index_alto]}, Peso {pesos[index_alto]} Kg, Altura {altura_max} cm')
print(f'Aluno mais baixo cod {codigos[index_baixo]}, Peso {pesos[index_baixo]} Kg, Altura {altura_min} cm')
