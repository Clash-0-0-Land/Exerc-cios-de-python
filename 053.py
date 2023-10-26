frase= input('Digite uma frase: ').strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
#inverso= ''
inverso1= junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso+= junto[letra]'''
print('O inverso de {} é {}.' .format(junto, inverso1))
if inverso1 == junto:
    print('Temos um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
