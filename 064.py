print('''DIGITE UM NÚMEROS QUANTAS VEZES QUISER. 
NO FIM, DAREMOS A QUANTIDADE DE NÚMEROS QUE VOCÊ DIGITOU E A SOMA DELES.
PARA SAIR DO PROGRAMA, DIGITE 999.''')
print('=-='*30)
c = t = d = 0
c= int(input('Digite um número (999 para parar): '))
while c != 999:
    d+=c
    t+=1
    c = int(input('Digite um número (999 para parar): '))
print('O resultado da soma dos {} números digitados é {}.'.format(t, d))