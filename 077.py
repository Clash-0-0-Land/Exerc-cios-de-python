tupla = ('VENTILADOR', 'COMPUTADOR', 'NOTEBOOK', 'CAMA', 'PROGRAMAR',
         'CADEIRA', 'CELULAR', 'ESCOVA', 'LIVRO', 'CANETA',
         'MERCADO', 'COMIDA', 'MALHAR', 'BRINCAR', 'PYTHON')
print('='*50)
print(f'\033[36m{"ANÁLISE DE VOGAIS":^50}\033[m')
print('='*50)
for c in tupla:
    print(f'\nA palavra "{c}" tem as vogais: ', end='')
    for letra in c:
        if letra in 'AÂÃÉÊEIÍOÓÔU':
            print(f'\033[31m{letra.upper()}\033[m ', end='')