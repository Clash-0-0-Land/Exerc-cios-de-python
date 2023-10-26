from random import randint
from time import sleep
cont= 0
while True:
    jogador= 0
    computador = randint(1, 11)
    escolha = ' '
    print('='*30)
    print ('''   VAMOS JOGAR PAR OU ÍMPAR''')
    print('='*30)
    while escolha not in 'PI':
        escolha = str(input('Escolha IMPAR ou PAR: [P/I] ')).upper().strip()[0]
    if escolha == 'I':
        print('OK. Eu sou Par e você é Ímpar.')
    if escolha == 'P':
        print('OK. Eu sou Ímpar e você é Par.')
    while True:
        jogador= int(input('Digite seu lance: '))
        if jogador>0:
            break
    total = computador + jogador
    print('LÁ VAI!')
    sleep(1)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    print(f'Eu escolhi {computador}.')
    print(f'{jogador} + {computador} = {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print ('DEU PAR')
            print ('PARABÉNS, VOCÊ GANHOU!')
            cont+=1
        else:
            print('DEU IMPAR')
            print ('VOCÊ PERDEU.')
            break
    if escolha == 'I':
        if total % 2 == 1:
            print('DEU IMPAR')
            print ('PARABÉNS, VOCÊ GANHOU!')
            cont+=1
        else:
            print('DEU PAR')
            print ('VOCÊ PERDEU.')
            break
print(f'VOCÊ GANHOU {cont} VEZES CONSECUTIVAS.')