times= ('América Mineiro', 'Atlético-PR', 'Atlético-MG', 'Bahia', 'Botafogo',
        'Corinthians', 'Coritiba', 'Cruzeiro',
        'Cuiabá', 'Flamengo',
        'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
        'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')

print(f'TIMES DO BRASILEIRÃO: {times}')
print('=-='*30)
print(f'\033[32mOs 5 primeiros colocados são: {times[0:5]}\033[m')
print('=-='*30)
print(f'\033[36mOs 4 últimos colocados são: {times[-4:]}\033[m')
print('=-='*30)
print(f'\033[35mOrdem alfabética dos times: {sorted(times)}\033[m')
print('=-='*30)
print(f'\033[31mO Flamengo está na {times.index("Flamengo")+1}ª posição.\033[m')
