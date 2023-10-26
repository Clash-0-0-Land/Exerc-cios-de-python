n= input ('Qual é o nome da cidade em que você mora? ')
verificar = 'Santo' in n
if verificar == True:
    print ('{} possui a palavra Santo.' .format(n))
else:
    print ('{} não possui a palavra Santo.'.format(n))