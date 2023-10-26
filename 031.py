n= int(input('Qual é a distancia da viagem em quilômetros? '))
p= n*0.50
q= n*0.45
if n <= 200:
    print('Você terá de pagar R${:.2f}.' .format(p))
else:
    print ('Você terá de pagar R${:.2f} pela passagem.' .format(q))