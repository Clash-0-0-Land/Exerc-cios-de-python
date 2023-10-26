def ficha(jogador, gols):
    global jogador1
    global gols1
    jogador1 = jogador
    gols1 = gols
    if jogador == '' and gols == '':
        jogador1= '<desconhecido>'
        gols1='0'
    elif jogador == '':
        jogador1= '<desconhecido>'
    elif gols == '':
        gols1= '0'
    print(f'O jogador {jogador1} marcou {gols1} gol(s).')
jogador1= str(input('Nome do jogador: ')).strip()
gols1= str(input('Nº de gols: ')).strip()
ficha(jogador1, gols1)
