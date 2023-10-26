n= int(input('Qual é o salário do funcionário A? '))
por= (n*10)/100
cen= por+n
ta= (n*15)/100
gem= ta+n
if n <= 1250:
    print ('O funcionário A receberá um aumento de 15%, portanto, ele passará a ganhar R${:.2f}.' .format(gem))
else:
    print('O funcionário A receberá um aumento de 10%, portanto,  ele passará a ganhar R${:.2f}.' .format(cen))