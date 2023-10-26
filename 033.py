n= int(input('Qual é o primeiro número? '))
n2= int(input('Qual é o segundo número? '))
n3= int(input('Qual é o terceiro número? '))
maior= n
menor= n

if (n2>n) and (n2>n3):
     maior=n2

if (n3>n) and (n>n3):
     maior= n3

if (n2<n) and (n2<n3):
     menor= n2

if (n3<n) and (n<n3):
     menor=n3

print('O maior valor digitado foi {}.' .format(maior))
print('O menor valor digitado foi {}.' .format(menor))