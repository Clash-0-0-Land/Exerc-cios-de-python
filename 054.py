from datetime import date
s= 0
r= 0
for c in range (1, 8):
    ano= int(input('Qual é o ano de nascimento da {}ª pessoa? ' .format(c)))
    atual= date.today().year
    t= atual-ano

    if t >= 18:
        s= s+1
    if t<18:
        r+= 1
if s > 1:
    print('{} pessoas já atingiram a maioridade.\n{} ainda são menores de idade.' .format(s, r))
elif s == 1:
    print('Apenas 1 pessoa atingiu a maioridade.\n {} ainda são menores de idade.'.format(r))
else:
    print('Nenhuma pessoa atingiu a maioridade.')

