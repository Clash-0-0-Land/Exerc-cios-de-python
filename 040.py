n1= float(input('Qual é a sua nota no 1º bimestre? '))
n2= float(input('Qual é a sua nota no 2º bimestre? '))
n3= float(input('Qual é a sua nota no 3º bimestre? '))
n4= float(input('Qual é a sua nota no 4º bimestre? '))

ma= (n1+n2+n3+n4)/4

if ma < 5:
    print ('\033[31mREPROVADO!\033[m')
elif ma >= 5.0 and ma <=6.9:
    print ('\033[33mRECUPERAÇÃO.\033[m')
elif ma >= 7.0:
    print ('\033[32mAPROVADO!\033[m')