def maior (*num):
    m = 0
    lista=[]
    print('-='*20)
    print('Analizando os valores passados.')
    lista.append(num)
    for q in range(0, len(num)):
        print(f'{lista[0][q]}', end=' ')
        if q == 0:
            m= lista[0][q]
        else:
            if lista[0][q] > m:
                m = lista[0][q]
    print(f'foram informados e {int(len(num))} números ao todo.', end='')
    print(f'\nO maior valor foi {m}.')
    print(f'-='*20)
maior(9,644,3,4)