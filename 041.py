from datetime import date
nasc= int(input('Digite seu ano de nascimento: '))
atual= date.today().year
idade= atual - nasc

if idade <= 9:
    print ('O atleta tem {} anos.' .format(idade))
    print ('Categoria: MIRIM')
elif idade > 9 and idade<=14:
    print('O atleta tem {} anos.'.format(idade))
    print ('Categoria: INFANTIL')
elif idade > 14 and idade <=18:
    print('O atleta tem {} anos.'.format(idade))
    print ('Categoria: JUNIOR')
elif idade > 18 and idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print ('Categoria: SÊNIOR')
elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print ('Categoria: MASTER')