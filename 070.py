nome= 'A'
preço = 0
pergunta= 'q'
soma= 0
cont= 0
cont1= 0
barato= 0
produtobarato= 'a'
while True:
    print('='*30)
    cont1+=1
    nome= str(input('Nome do produto: '))
    preço= float(input('Preço: R$'))
    soma += preço
    if preço > 1000:
        cont+=1

    if cont1 == 1 or preço < barato:
        barato= preço
        produtobarato= nome

    while True:
        pergunta= str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
        if pergunta in 'SN':
            break
    if pergunta == 'N':
        break
print('---------- ESTATÍSTICAS DE COMPRA ----------')

print(f'''TOTAL GASTO: R${soma:.2f}
PRODUTOS COM PREÇO ACIMA DE R$1000,00: {cont}
PRODUTO MAIS BARATO: {produtobarato} (R${barato:.2f})''')