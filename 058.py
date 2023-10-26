from random import randint
computador= randint (0, 10)
print('Olá, eu sou seu computador.')
print('Vamos jogar um jogo? Será que você consegue adivinhar?')
acertou= False
palpite= 0
while not acertou:
    jogador= int(input('Adivinhe qual foi o número que eu escolhi de 0 a 10: '))
    palpite+=1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador < computador:
            print('Menos...  Tente novamente.')
print('Você deu {} palpites até acertar. Parabéns, você ganhou.' .format(palpite))
