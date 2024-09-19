import os
os.system('cls')

contador = 1
cont = 0

codigos = []
veiculos = []
acidentes = []
indice_acidentes = []
acima_2k_veiculos_acidentes = []

while cont < 5:
    codigo = int(input(f'Digite o codigo da {contador}º cidade:  '))
    codigos.append(codigo)
    os.system('cls')

    veiculo = int(input(f'Digite o numero de veiculos de passeio na {contador}º cidade: '))
    veiculos.append(veiculo)
    os.system('cls')

    acidente = int(input(f'Digite a quantidade de acidentes na {contador}º cidade:  '))
    acidentes.append(acidente)
    os.system('cls')

    if acidente > 0:  
        indice_acidente = veiculo / acidente
    else:
        indice_acidente = float('inf')  
    indice_acidentes.append(indice_acidente)

    if veiculo < 2000:
        acima_2k_veiculos_acidentes.append(acidente)

    contador += 1
    cont += 1

media_veiculos = sum(veiculos) / 5
media_2k = sum(acima_2k_veiculos_acidentes) / len(acima_2k_veiculos_acidentes) if acima_2k_veiculos_acidentes else 0

indice_min = min(indice_acidentes)
indice_max = max(indice_acidentes)

index_MEIA = indice_acidentes.index(indice_min)
index_MAIA = indice_acidentes.index(indice_max)

print(f'O menor índice de acidentes é {indice_min:.2f} e pertence à cidade com código {codigos[index_MEIA]}')
print(f'O maior índice de acidentes é {indice_max:.2f} e pertence à cidade com código {codigos[index_MAIA]}')
print(f'A média de veículos nas 5 cidades é {media_veiculos:.2f}')
print(f'A média de acidentes nas cidades com menos de 2000 veículos é de {media_2k:.2f}')
