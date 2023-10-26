n= int(input('Qual a largura da parede? '))
n1= int(input('Qual a altura? '))
n2= int(input('Quantos mestros quadrados a lata de tinta pode pintar? '))
s= n*n1
r= s//n2
print ('Você precisará de {}l de tinta.' .format(r))