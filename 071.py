print('='*30)
print('       BANCO 24 HORAS    ')
print('='*30)
pergunta = int(input('DIGITE O VALOR A SER SACADO: R$'))
saldo= pergunta
ced= 50
totced= 0
while True:
    if saldo >= ced:
        saldo -= ced
        totced += 1
    else:
        if totced> 0:
          print(f'Total de {totced} cédulas de R${ced:.2f}')
        elif ced==50:
            ced= 20
        elif ced == 20:
            ced= 10
        elif ced == 10:
            ced= 1
        elif ced== 1:
            ced= 0
        totced= 0
        if ced == 0:
            break
print('='*30)
print('O BANCO 24 HORAS AGRADECE A SUA PREFERÊNCIA. VOLTE SEMPRE!')