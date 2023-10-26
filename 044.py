print ('{:=^40}' .format(' LOJAS VASCONCELOS '))
preçop= float(input ('Qual é o preço do produto? R$'))
pagamento= int(input('''FORMAS DE PAGAMENTO:
[ 1 ] À vista no dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] Em até 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)
Digite uma das opçôes: '''))

if pagamento == 1:
    preço= preçop - (preçop*10) / 100

elif pagamento == 2:
    preço= preçop-(preçop*5) / 100

elif pagamento == 3:
    preço= preçop

elif pagamento == 4:
    parcelas= int(input('Quantas parcelas? '))
    if parcelas >= 3:
        preçoparcelas= parcelas + ((preçop*20)/100)
        preço= preçop+preçoparcelas
        print ('Sua compra de R${:.2f} foi de dividida em {}x de R${}.' .format (preçop, parcelas, preçoparcelas))
    else:
        preço= preçop
else:
    preço = 0
    print ('\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m')

print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preçop, preço))