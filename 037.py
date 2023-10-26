n= int(input('Digite um número: '))
print('''Opções:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
n2= int(input('Escolha uma das opções acima: '))

if n2 == 1:
    print(format(n, 'b'))
elif n2 == 2:
    print(format(n, 'o'))
elif n2==3:
    print(format(n, 'x'))
else:
    print ('Opção inválida. Por favor, tente novamente.')