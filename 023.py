n= input('Digite um número de 0 a 9999: ')
s= '000' + n
a= s[-1]
b= s[-2]
c= s[-3]
d= s[-4]
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(a, b, c, d))