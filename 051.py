print('='*32)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('='*32)
n= int(input('PRIMEIRO TERMO: '))
r= int(input('RAZÃO: '))
decimo= n+(10-1)*r
for c in range(n, decimo+1, r):
    print ('{} --> '.format(c),end='')
print('ACABOU',end='')