tp= (int(input('Digite um número: ')),
    int(input('Digite um número mais uma vez: ')),
    int(input('Digite um número novamente: ')),
    int(input('Digite um número pela última vez: ')))

print(f'Os valores digitados foram: {tp}')
print(f'O número 9 apareceu {tp.count(9)} vezes.')
if 3 in tp:
    print(f'O número 3 está na {tp.index(3)+1}ª posição.')
else:
    print('O número 3 não foi registrado.')
print('Os número pares são: ', end='')
for p in tp:
    if p % 2 == 0:
        print(f'{p}', end=' ')
