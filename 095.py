jogador = {}
lista= []
todos_jogadores= []
resp= 'S'
resp2= 0
while resp !=  'N':
    print('='*50)
    jogador['nome'] = str(input('Nome do jogador: '))
    part= int(input('Número de partidas: '))
    for q in range(0, part):
        lista.append(int(input(f'Quantos gols na partida {q}? ')))
    jogador['gols']= lista[:]
    jogador['total']= sum(lista)
    todos_jogadores.append(jogador.copy())
    lista.clear()
    while True:
        resp= str(input('Deseja continuar? [S/N] '))[0].upper().strip()
        if resp in 'SN':
            break
        print('\033[31mERRO! Responda S ou N\033[m')
print('='*40)
print('CÓD ', end='')
for g in jogador.keys():
    print(f'{g:<15} ', end= '')
print()
for k, v in enumerate(todos_jogadores):
    print(f'{k:>3} ', end='')
    for q in v.values():
        print(f'{str(q):<15}', end ='')
    print('')
print('-'*40)
while resp2 != 999:
    resp2= int(input('Mostrar levantamento de qual jogador? (999 para sair) '))
    if resp2 >= len(todos_jogadores) and resp2 != 999:
        print('\033[31mERRO! Jogador não encontrado. Por favor, tente novamente.\033[m')
    for q in range(0, len(todos_jogadores)):
        if resp2 == q:
            print(f'>> LEVANTAMENTO DO JOGADOR {todos_jogadores[q]["nome"]}:')
            for g in range(0, len(todos_jogadores[q]['gols'])):
                print(f'    Na partida {g} fez {todos_jogadores[q]["gols"][g]} gols.')
    print('='*50)
print(f' \033[35m{"<< ATÉ MAIS! >>".center(50)}\033[m ')