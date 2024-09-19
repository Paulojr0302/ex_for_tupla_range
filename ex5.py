import os
os.system('cls')

lista = []
contador=0
cont=1
vogal = 0
consoante = 0

print('Digite 10 caracteres:  ')

while contador < 10:
    caractere = input(f'Digite o {cont}º caractere: ')
    contador +=1
    cont+=1

    if(caractere == 'a' or caractere == 'e' or caractere =='i' or caractere =='o' or caractere=='u'):
        vogal +=1
    
    else:
        lista.append(caractere)
        consoante +=1
    os.system('cls')

print(lista)
print('Total consoantes: ',consoante)
print('Total vogais',vogal)

    
