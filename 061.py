print('='*13)
print('GERADOR DE PA')
print('='*13)
p= int(input('PRIMEIRO TERMO: '))
r= int(input('RAZÃO: '))
c= 0
t= p
while c <= 10:
    print('{} --> '.format(t), end='')
    t+=r
    c+=1
print('FIM', end='')