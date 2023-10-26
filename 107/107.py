from moeda import *

p= int(input('Valor: R$'))
print(f'O dobro de {p} é {dobro(p)}')
print(f'A metade de {p} é {metade(p)}')
print(f'{p} teve um aumento de 10%, passando a ser {aumentar(p, 10)}')
print(f'{p} teve um desconto de 10%, passando a ser {descontar(p, 10)}')