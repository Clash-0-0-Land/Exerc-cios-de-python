def área(a, b):
    r= a*b
    print(f'A área de um terreno {a}x{b} é igual a {r}m².')
def title(msg):
    print('='*30)
    print(msg)
    print('='*30)
title('     Controle de terreno     ')
x= float(input('COMPRIMENTO (m): '))
y= float(input('LARGURA (m): '))
área(x, y)