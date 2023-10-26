cont= cont2= cont3= media= 0
cadastro= {}
pessoas= []
mulheres= []
resp = 'S'
while resp[0] != 'N':
    cadastro['nome'] = str(input('Nome: '))
    cadastro['idade'] = int(input('Idade: '))
    cadastro['sexo']= str(input('Sexo [M/F]: '))[0].upper()
    pessoas.append(cadastro.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] '))[0].strip().upper()
        if resp in 'SN':
            break
        else:
            print('\033[31mERRO! Responda apenas S ou N!\033[m')
print('-='*30)
print(f'A) {len(pessoas)} pessoas foram cadastradas.')
for f in range(0, len(pessoas)):
    cont3+= pessoas[f]['idade']
media= cont3/len(pessoas)
print(f'B) A média da idade entre essas pessoas é {media:.2f} anos')
print(f'C) Ao todo, foram cadastradas {cont} mulheres, sendo elas:', end=' ')
for q in range(0, len(pessoas)):
    if pessoas[q]['sexo'] == 'F':
        print(pessoas[q]['nome'], end='')
print(f'\nD) lista das pessoas com idade acima da média: ')
for g in pessoas:
    if g['idade'] >= media:
        print('     ')
        for k, v in g.items():
            print(f'    {k} = {v} ', end='')
        print()
print('\n<< ENCERRADO >>')