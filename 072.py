n= ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    p= int(input('Digite um número de 0 a 20: '))
    if 0 <= p  <= 20:
        print(f'\033[36mVocê digitou o número {n[p]}.\033[m')
        con= str(input('Deseja continuar? [Sim/Não]')).upper().strip()[0]
        if con == 'S':
            continue
        if con== 'N':
            break
    print('ERRO! TENTE NOVAMENTE.', end=' ')