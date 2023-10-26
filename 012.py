n= int(input('Quanto vale o produto? '))
r= n/100*5
rf= n-r
print ('O produto de R${} passará a valer R${} com o desconto de 5% aplicado.'
       .format(n, rf))