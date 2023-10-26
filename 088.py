import random as aleatorio
import time as segundo
tot=1
print('='*30)
print(f'PALPITES DA MEGA CENA'.center(30))
print('''='''*30)
lista = []
lista2 = []
np= int(input('Quantos palpites você deseja? '))
while tot <= np:
    cont=0
    while True:
        num = aleatorio.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
    tot+=1
print(f'=-=-=-=SORTEANDO {np} JOGOS=-=-=-='.center(30))
for c, g in enumerate(lista2):
    print(f'\033[34mJogo {c+1}: {g}\033[m')
    segundo.sleep(1)
print('-=-=-=-=-=BOA SORTE=-=-=-=-=-=-'.center(30))