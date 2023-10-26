ficha= []
nota1= nota2 = media = 0
while True:
    print('-'*31)
    nome = str(input('Nome: '))
    nota1= float(input('Nota 1: '))
    nota2= float(input('Nota2: '))
    media= (nota1+nota2)/2
    ficha.append([nome,[nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'Não' or resp == 'NAO':
        break
print(ficha)
print('='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}', end='')
    print(f'{a[0]:<10}',end='')
    print(f'{a[2]:>8}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('-=-=-=-=-=BOA SORTE=-=-=-=-=-')
