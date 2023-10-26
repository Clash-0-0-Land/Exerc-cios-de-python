
v= int(input('Em km/h, qual é a velocidade do seu carro? '))
if v <= 80:
    print('Ótimo, continue assim.')
else:
    print('Com a multa de R$7.00 para cada quilômetro que está sendo rodado acima do limite, você terá de pagar R${:.2f}.' .format((v-80)*7))