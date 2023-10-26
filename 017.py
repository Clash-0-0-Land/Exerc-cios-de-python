import math
n= float(input('Qual é o comprimento do cateto oposto? '))
m= float(input('Qual é o comprimento do cateto adjacente? '))
q= math.hypot(n, m)
print ('O resultado é {:.2f}.' .format(q))