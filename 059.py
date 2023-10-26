from time import sleep
print('\033[36m===== DIGITE DOIS NÚMEROS =====\033[m')

t= int(input('Digite um valor: '))
g= int(input('Digite ouro valor: '))
maior= 0
h=0
while h != 5:
    print('=========================================')
    h= int(input('''Escolha uma das operações:
\033[33m[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA\033[m
>>>>>> Digite uma das opções: '''))
    if h == 1:
        print('{}+{}={}'.format(t, g, t+g))
    elif h == 2:
        print('{}x{}={}'.format(t, g, t*g))
    elif h == 3:
        maior = t
        if t == g:
            print('Ambos os valores são iguais.')
        elif maior > g:
            maior = t
            print('O maior número é o {}.' .format(maior))
        else:
            maior = g
            print('O maior número é o {}.' .format(maior))
    elif h == 4:
        print('\033[34mEscolha novos números.\033[m')
        g= int(input('Digite um valor: '))
        t= int(input('Digite outro valor: '))

    elif h == 5:
        print('SAINDO DO PROGRAMA...')
        print('=-='*15)
    else:
        print('\033[31mERRO! TENTE NOVAMENTE!\033[m')
    sleep(2)
print('PROGRAMA FINALIZADO.')