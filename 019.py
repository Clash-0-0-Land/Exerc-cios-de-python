import random
a = input('Qual é o aluno 1? ')
b = input('Qual é o aluno 2? ')
c = input('Qual é o aluno 3? ')
d = input('Qual é o aluno 4? ')
lista= (a, b, c, d)
m= random.choice(lista)
print('O aluno sorteado foi {}. Parabéns!'.format(m))
