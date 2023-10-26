from datetime import date
atual= date.today().year
nasc= int(input('Qual é o seu ano de nascimento? '))
idade= atual-nasc

if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))
    print('Você tem que se alistar IMEADIATAMENTE!')

elif idade > 18:
    saldo= idade-18
    print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))
    print ('Já se passou {} ano(s) desde o seu ano de alistamento.' .format(saldo))
    print ('Você deveria ter se alistado em {}.' .format (atual-saldo))

elif idade < 18:
    saldo= 18-idade
    print('Quem nasceu em {} tem {} anos em {}.' .format (nasc, idade, atual))
    print('Falta {} ano(s) para você se alistar.' .format(saldo))
    print('Você tem que se alistar em {}.' .format(saldo+atual))