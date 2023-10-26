import random
print ('Vamos jogar jokenpô!')
n= int(input('Escolha:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\nDigite sua jogada: '))
p1= 'Pedra'
p2= 'Papel'
p3= 'Tesoura'
lista= (p1, p2, p3)
p= random.choice (lista)

print ('Jo')
print('Ken')
print('Pô!!!')
print('='*30)
print('COMPUTADOR: {}' .format(p))
if n== 1:
    print('JOGADOR: Pedra')
elif n==2:
    print('JOGADOR: Papel')
elif n==3:
    print('JOGADOR: Tesoura')
else:
    print('JOGADOR: ')
print('='*30)

if n == 1 and p == p1:
    print('EMPATE')
    print ('Opa, deu um empate. Vamos de novo.')
elif n == 1 and p == p3:
    print('JOGADOR VENCE')
    print ('Caramba, você é bom mesmo! Vamos jogar de novo pois dessa vez eu irei ganhar.')
elif n == 1 and p == p2:
    print ('COPUTADOR')
    print ('Hehe, eu ganhei! Vamos outra para que você perca para mim novamente.')

elif n == 3 and p == p3:
    print('EMPATE')
    print ('Opa, deu um empate. Vamos de novo.')
elif n == 3 and p == p1:
    print('JOGADOR VENCE')
    print ('Caramba, você é bom mesmo! Vamos jogar de novo pois dessa vez eu irei ganhar.')
elif n == 3 and p == p2:
    print ('COMPUTADOR VENCE')
    print ('Hehe, eu ganhei! Vamos outra para que você perca para mim novamente.')

elif n == 2 and p == p2:
    print('EMPATE')
    print ('Opa, deu um empate. Vamos de novo.')
elif n == 2 and p == p1:
    print('JOGADOR VENCE')
    print ('Caramba, você é bom mesmo! Vamos jogar de novo pois dessa vez eu irei ganhar.')
elif n == 2 and p == p3:
    print ('COMPUTADOR VENCE')
    print ('Hehe, eu ganhei! Vamos outra para que você perca para mim novamente.')

else:
    print ('\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m')