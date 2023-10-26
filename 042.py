r1= float(input('Primeira reta: '))
r2= float(input('Segunnda reta: '))
r3= float(input('Terceira reta: '))

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('É possível formar um triãngulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print ('ISÓSCELES.')
    else:
        print ('ESCALENO.')

else:
    print ('Não é possível formar um triângulo.')