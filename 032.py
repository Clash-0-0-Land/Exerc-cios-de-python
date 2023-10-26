n= int(input('Qual é o ano? '))
if (n % 4) == 0:
    print('O ano {} é bissexto.' .format(n))
else:
    print ('Ano {} não é bissexto' .format(n))