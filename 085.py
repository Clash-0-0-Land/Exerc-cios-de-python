num = [[], []]
for q in range(0, 7):
    d = int(input('Digite um valor: '))
    if d % 2 == 0:
        num[0].append(d)
        num[0].sort()
    else:
        num[1].append(d)
        num[1].sort()
print('-='*60)
print(f'Os valores pares digitados foram: {num[0]}.')
print(f'Os valores impares digitados foram: {num[1]}.')