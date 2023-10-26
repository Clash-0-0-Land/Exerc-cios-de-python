n= input('Qual é a matéria? ')
n1= float(input('Qual é a sua nota no 1º bimestre? '))
n2= float(input('Qual é a sua nota no 2º bimestre? '))
n3= float(input('Qual é a sua nota no 3º bimestre? '))
n4= float(input('Qual é a sua nota no 4º bimestre? '))
rf= n1+n2+n3+n4
print ('A sua média anual em {} é de {} pontos.' .format(n, (rf/4)))