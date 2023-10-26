p= 'S'
g= 0
y= 0
maior= 0
menor= 0
contador= 0
while p in 'Ss':
    contador+=1
    y= int(input('DIGITE UM VALOR: '))
    g= y+g
    if contador == 1:
        maior = y
        menor = y
    else:
        if y > maior:
            maior= y
        if y < menor:
            menor=y
    p = input('DESEJA CONTINUAR? [S/N] ').upper().strip()[0]
média= g/contador
print('''Você digiou {} números e a média desses valores foi {:.2f}.
O maior número digitado foi {} e o menor foi {}.'''. format(contador, média, maior, menor ))
