tupla= ('Lápis', 1.00,
        'Borracha', 1.50,
        'Caderno 20 matérias', 62.90,
        'Caderno 10 matérias', 32.50,
        'Canetas Bic', 1.50,
        'Canetas Faber-Castel',2.50,
        'Estojo', 21.49,
        'Mochila', 70.89)

print('='*60)
print ('PAPELARIA COSTA E SILVA'.center(60))
print('='*60)
cont=0
for pos in range(0, len(tupla)):
        cont+=1
        if pos % 2 == 0:
                print (f'{tupla[pos]:.<51}', end='')
        else:
                print(f'R${tupla[pos]:>7.2f}')
print('='*60)