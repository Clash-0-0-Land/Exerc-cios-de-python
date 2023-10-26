def voto(a):
    import datetime
    b = datetime.date.today().year
    idade = b-a
    print(f'Com {idade} anos: ',end='')
    if idade < 18:
        print('Não pode votar', end='')
    elif idade >= 18 and idade < 65:
        print('Voto obrigatório.', end='')
    else:
        print('Voto opcional.', end='')
print('='*20)
ano= int(input('Ano de nascimento: '))
voto(ano)