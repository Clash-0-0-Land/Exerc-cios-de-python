n= s= c= 0
while True:
    n= int(input('Digite um número: [Caso deseje sair, digite 999] '))
    if n == 999:
        break
    s+=n
    c+=1
print(f'Foram digitados {c} números.\nA soma deles vale {s}.')
