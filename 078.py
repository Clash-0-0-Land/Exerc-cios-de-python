lista = []
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('-=' * 30)
print(f'você digitou os valores {lista}')
print(f'O maior valor foi {mai} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f' {i}...', end='')
print('')
print(f'O menor valor foi {men} e está nas posições',end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f' {i}...', end='')