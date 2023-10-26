from time import sleep
def contador(inicio, fim, passo):
    print()
    print('-='*20)
    if passo < 0:
        passo*=(-1)
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    soma= 0
    cont= 0
    if inicio > fim:
        while soma != fim:
            cont += 1
            if cont == 1:
                soma = inicio
            print(f'{soma}->', end='')
            soma = soma - passo
            sleep(1)
            if soma < fim:
                break
        if soma == fim:
            print(f'{soma}->', end='')
        print('FIM', end='')
    if inicio < fim:
        while soma <= fim:
            cont+=1
            if cont == 1:
                soma = inicio
            print(f'{soma}->', end='')
            soma = soma + passo
            sleep(1)
        print('FIM', end= '')
contador (0, 10, 1)
contador (10, 0, 2)
print()
print('-='*20)
i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
contador(i, f, p)