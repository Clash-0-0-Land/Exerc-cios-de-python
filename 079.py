num = list()
while True:
    p= int(input('Digite um número: '))
    if p not in num:
        num.append(p)
        print('Valor adicionado com sucesso.')
    else:
        print('\033[31mValor duplicado! Não adicionado à lista.\033[m')
    p2= str(input('\033[36mDeseja continuar? [S/N] \033[m')).upper()
    if p2 in 'NNÃO':
        break
num.sort()
print(f'Os números em ordem crescente são: {num}')