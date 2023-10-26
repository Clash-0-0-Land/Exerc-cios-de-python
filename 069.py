cont=cont2=cont3=0
while True:
    pergunta2= 'E'
    pergunta3= 'Z'
    print('='*30)
    print('     CADASTRE UMA PESSOA     ')
    print('='*30)
    pergunta= int(input('Quantos anos você tem? '))
    while True:
        pergunta2= str(input('Qual seu sexo? (M/F) ')).upper().strip()[0]
        if pergunta2 in 'MF':
            break
    print('='*30)
    while True:
        pergunta3= str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
        if pergunta3 in 'SN':
            break
    if pergunta >= 18:
        cont+=1
    if pergunta2 == 'M':
        cont2+=1
    if pergunta2 == 'F' and pergunta >= 20:
        cont3+=1
    if pergunta3 == 'N':
        break
print('='*30)
print(f'''TOTAL DE PESSOAS COM IDADES ACIMA DE 18 ANOS: {cont}
HOMENS CADASTRADOS: {cont2}
MULHERES COM IDADES ACIMA DE 20 ANOS: {cont3}''')