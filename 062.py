print('='*13)
print('GERADOR DE PA')
print('='*13)
p= int(input('PRIMEIRO TERMO: '))
r= int(input('RAZÃO: '))
c= 0
t= p
total= 0
mais= 10
while mais != 0:
    total+=mais
    while c <= total:
        print('{} --> '.format(t), end='')
        t+=r
        c+=1
    print('PAUSA')
    mais= int(input('Mais quantos termos você quer a mais? '))
print('PROGRESSÃO FINALIZADA COM {} TERMOS.'.format(total))