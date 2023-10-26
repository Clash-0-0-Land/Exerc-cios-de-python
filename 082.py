l1 = []
l2 = []
l3 = []
while True:
    l1.append(int(input('Digite um número: ')))
    p = str(input(('DESEJA CONTINUAR? (S/N) '))).upper().strip()
    if p in 'NNÃO':
        break
for v, i in enumerate(l1):
    if v % 2 == 0:
        l2.append(i)
    if v % 2 == 1:
        l3.append(i)
print('=-'*30)
print(f'Lista com todos os valores: {l1}')
print(f'Lista com todos os valores pares: {l2}')
print(f'Lista com todos os valores ímpares: {l3}')