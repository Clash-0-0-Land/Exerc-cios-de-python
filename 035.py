r1= float(input('Comprimento da reta 1: '))
r2= float(input('Comprimento da reta 2: '))
r3= float(input('Comprimento da reta 3: '))

if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
            print('Com o valor da medida das retas, é sim possível formar um triângulo.')

else:
    print('Não é possível formar um triângulo.')

if r1==r2==r3:
    print ('É possível formar um triângulo.')