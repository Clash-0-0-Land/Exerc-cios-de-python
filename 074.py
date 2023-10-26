from random import randint
c1= (randint(0, 20), randint(0, 20),
     randint(0, 20), randint(0, 20), randint(0, 20))
print('Os número sorteados foram: ', end='')
for u in c1:
    print(f'{u}, ', end='')

print(f'\nO maior número sorteado foi {max(c1)}.')
print(f'O menor número sorteado foi {min(c1)}.')