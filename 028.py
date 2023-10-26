import random
p= int(input('Adivinhe qual foi o número de 0 a 5 que o computador escolheu. '))
n= random.randint(0, 5)
if p == n:
    print('Parabéns, você acertou!')
else:
    print ('Errou feio, errou rude.')
print ('O número escolhido pelo computador foi {}.' .format(n))