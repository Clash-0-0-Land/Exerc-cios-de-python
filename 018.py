import math
n= float(input('Qual é o valor do ângulo? '))
c= math.cos(n)
s= math.sin(n)
t= math.tan(n)
print ('O seno de {} é {:.2f}\nO cosseno de {} é {:.2f}.\nA tangente de {} é {:.2f}.'
       .format (n, s, n, c, n, t))