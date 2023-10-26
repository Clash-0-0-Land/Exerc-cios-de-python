def factorial(número, show=False):
    '''
    factorial(número, show=False)
    :param número: número a calcular seu factorial
    :param show: se for igual a True, mostra a conta. Senão, mostra apenas o resultado
    :return: retorna o valor final do fatorial do número
    '''
    print('='*30)
    if show == True:
        valor= 1
        for cont in range(número, 0, -1):
            if cont == 1:
                print(f'{cont} = ', end='')
            else:
                print(f'{cont} x ',end='')
            valor*=cont
        return valor
    else:
        valor = 1
        for cont in range(número, 0, -1):
            valor *= cont
        return valor
help(factorial)