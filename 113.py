def leiaFloat(a=''):
    while True:
        try:
            valor = float(input(f'{a}'))
            if valor == int(valor):
                pass
        except ValueError:
            print(f'\033[31mValor real inválido.\033[m')
        except KeyboardInterrupt:
            print('\nNão foi informado nada, portanto o valor é 0.')
            valor = 0
            print(f'O valor real informado foi {valor}.')
            break
        else:
            print(f'O valor real informado foi {valor}.')
            break

def leiaInt(a=''):
    while True:
        try:
            valor = int(input(f'{a}'))
        except ValueError:
            print(f'\033[31mValor inteiro inválido.\033[m')
        except KeyboardInterrupt:
            print('\nNão foi informado nada, portanto o valor é 0.')
            valor = 0
            print(f'O valor inteiro informado foi {valor}.')
            break
        else:
            print(f'O valor inteiro informado foi {valor}.')
            break

leiaInt('Digite um número inteiro: ')
leiaFloat('Digite um valor real: ')