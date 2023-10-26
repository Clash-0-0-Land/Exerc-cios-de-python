números= []
def sorteia(a):
    import random
    import time
    for q in range(0, 5):
        a.append(random.randint(0, 20))
    print(f'Sorteando 5 valores: ', end='')
    for d in range(0, len(a)):
        print(f'{a[d]}', end=' ')
        time.sleep(0.5)
sorteia(números)

def somapar(a):
    soma= 0
    for q in números:
        if q % 2 == 0:
            soma+=q
    print(f'\nA soma dos valores pares de {a} é igual {soma}.')
somapar(números)