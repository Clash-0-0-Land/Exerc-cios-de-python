'''lista = []
lista2 = []
for q in range (0, 5):
  res= int(input('Digite um valor numérico: '))
  lista.append(res)
for cont in range(0, 5):
  menor = 0
  menor = min(lista)
  lista2.append(menor)
  lista.remove(min(lista))
print(lista2)'''

lista = []
for c in range(0, 5):
  n = int(input('Digite o valor numérico: '))
  if c == 0 or n > lista[-1]:
    lista.append(n)
    print('Adicionando ao final da lista.')
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        print(f'Adicionando na posição {pos} da lista...')
        break
      pos+=1
print('-='*30)
print(f'Os valores digitados em ordem crescente são: {lista}')
