jogador = {}
lista= []
jogador['nome'] = str(input('Nome do jogador: '))
part= int(input('Número de partidas: '))
for q in range(0, part):
    lista.append(int(input(f'Quantos gols na partida {q}? ')))
print('-='*30)
jogador['gols']= lista[:]
jogador['total']= sum(lista)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f"O jogador {jogador['nome']} jogou {part} partidas:")
for cont in range(0, len(lista)):
    print(f'    -->> Na partida {cont}, fez {lista[cont]} gols.')
print(f"O total de gols é {jogador['total']}.")