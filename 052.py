n= int(input('Digite um número: '))
p= 0
for c in range(1, n+1):
    if n % c == 0:
        p= p+1
        print('\033[32m', end= ' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

if p == 2:
    print('\n\033[m{} tem {} números divisíveis por 2, portanto\nele é um número primo'.format(n, p))

else:
    print('\n\033[m{} tem {} número divisíveis por 2, portanto, portanto\nele não é um número primo.'.format(n, p))


