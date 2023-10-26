#FATORIAL EM "WHILE"
'''n= int(input('Digite o úmero que você deseja saber o FATORIAL: '))
c= n
f= 1
print('O fatorial desse número é:\n{}! = '.format(n, n), end= '')
while c != 0:
    print('{}'.format(c),'x ' if c > 1 else '=', end='')
    f*=c
    c-=1
print(' {} ' .format(f), end='')'''

#FATORIAL EM "FOR"
n= int(input('Digite o número que você deseja saber o fatorial: '))
f=1
print('O fatorial de {} é:'.format(n))
print('{}! = '.format(n), end='')
for c in range(n, 1, -1):
    print('{}'.format(c), 'x 'if c > 2  else 'x 1 =', end='')
    f*=c
print(' {}'.format(f), end='')