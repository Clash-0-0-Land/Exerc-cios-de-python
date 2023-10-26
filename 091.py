from time import sleep
from random import randint
from operator import itemgetter
jogo= {'jogador 1' : randint(1, 6),
       'jogador 2' : randint(1, 6),
       'jogador 3' : randint(1, 6),
       'jogador 4' : randint (1, 6)}
ranking= []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou o número {v}.')
    sleep(1)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse= True)
print('\nRanking dos jogadores: ')
for i, v in enumerate (ranking):
    print(f'     {i+1}º lugar: o {v[0]} tirou {v[1]} no dado.')
    sleep(1)