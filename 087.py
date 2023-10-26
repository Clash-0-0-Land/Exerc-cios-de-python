lista= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma=soma2=maior= 0
for d in range(0, 3):
    for q in range(0, 3):
        lista[d][q] = int(input(f'Digite o valor da casa ({d}:{q}): '))
print('-='*30)
for d in range(0, 3):
    for q in range(0,3):
        print(f'[{lista[d][q]:^5}]', end='')
        if lista[d][q] % 2 == 0:
            soma+=lista[d][q]
    print('')
print(f'A soma de todos os valores pares é: {soma}')
for d in range(0, 3):
    soma2+=lista[d][2]
print(f'A soma de todos os valores da 3ª coluna é: {soma2}')
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior número da 2ª linha é: {max(lista[1])}')