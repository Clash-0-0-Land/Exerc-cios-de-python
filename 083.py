n= str(input('Digite uma expressão: '))
lista1 = []
for simb in n:
    if simb == '(':
        lista1.append('(')
    elif simb == ')':
        if len(lista1) > 0:
            lista1.pop()
        else:
            lista1.append(')')
            break
if len(lista1) == 0:
    print('EXPRESSÃO VÁLIDA.')
else:
    print('EXPRESSÃO INVÁLIDA.')
