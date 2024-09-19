import os
os.system('cls')


temperatura = []
contador = 0
cont = 1
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('Digite a media de temperatura dos meses:')

for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperatura.append(temp)
    contador += 1
    os.system('cls')
    

media_anual = sum(temperatura) / len(temperatura)

print(f'A media anual de temperatura é {media_anual:.2f}ºC')

print("\nMeses com temperatura acima da média anual:")
for i in range(12):
    if temperatura[i] > media_anual:
        print(f"{i + 1} - {meses[i]}: {temperatura[i]:.2f}°C")

