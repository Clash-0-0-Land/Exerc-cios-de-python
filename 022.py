n=input('Digite seu nome completo: ')
t= n.upper()
r= n.lower()
j= n.replace(' ', '')
q= len(j)
prnome= n.split()
d= len(prnome[0])

print('O seu nome em letras maiúculas é {}.\nO seu nome em letras minúsculas é {}.\nO seu nome tem um total de {} letras.\nO seu primeiro nome tem {} letras.' .format(t, r, q, d))
