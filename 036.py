c= float(input('Qual é o valor da casa? '))
s= float(input('Qual é o valor do salário? '))

m= int(input('Em quantos anos você está disposto a pagar? '))
q= m*12

d= c/q
p= (30*s/100)
if d <= p:
    print ('Para fazer esse financiamento, você terá de pagar R${:.2f} por mês. Parabéns, seu empréstimo foi aprovado com êxito!' .format(d))
else:
    print ('Para fazer esse empréstimo, você terá de pagar R${:.2f} por mês. Infelizmente seu empréstimo não foi aprovado.' .format(d))