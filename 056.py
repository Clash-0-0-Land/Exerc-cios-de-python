somaidade= 0
homemvelho= 0
idadevelho=0
mava= 0
for c in range(1, 5):
    p= print('---- PESSOA Nº{} ----'.format(c))
    nome= input('Nome: ').strip()
    idade= int(input('Idade: '))
    sexo= input('Sexo [M/F]: ').strip()
    somaidade+= idade
    if c == 1 and sexo in 'Mm':
        homemvelho= nome
        idadevelho= idade
    if sexo in 'Mm' and  idade > idadevelho:
        idadevelho= idade
        homemvelho= nome
    if sexo in 'Ff' and idade < 20:
        mava= mava+1

mediaidade= somaidade/4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos de idade e se chama {}.' .format(idadevelho, homemvelho))
print('Há um total de {} mulheres com menos de 20 anos de idade.' .format(mava))