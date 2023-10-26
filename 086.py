lista= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for d in range(0, 3):
    for q in range(0, 3):
        lista[d][q] = int(input(f'Digite o valor da casa ({d}:{q}): '))
print('-='*30)
for d in range(0, 3):
    for q in range(0,3):
        print(f'[{lista[d][q]:^5}]', end='')
    print('')