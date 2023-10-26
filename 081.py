num= []
c= 0
while True:
    num.append(int(input('Digite um valor: ')))
    c+=1
    p2= str(input('DESEJA CONTINUAR? (S/N) ')).upper().strip()
    if p2 in 'NNÃO':
        break
num.sort(reverse=True)
print('=-'*30)
print(f'Você digitou {c} números.')
print(f'A ordem descrecente da lista é: {num}')
if 5 in num:
    print(f'O número 5 foi encontrado na lista.')
else:
    print('O número 5 não foi encontrado na lista.')