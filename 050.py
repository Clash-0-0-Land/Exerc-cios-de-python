p= 0
q= 0
for c in range (1, 7):
    n= int(input('Digite o {}º número: ' .format(c)))
    if n % 2 == 0:
        q+= 1
        p= p+n

if q == 0:
    print('Não há números pares.')
elif q == 1:
    print('Há somente um número par, que é {}.' .format(p) )
elif q > 1:
    print('A soma dos {} número pares que você informou é {}.' .format(q, p))