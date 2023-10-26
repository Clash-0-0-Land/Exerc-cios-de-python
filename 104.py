def leiaInt(a=''):
    while True:
        valor= input(f'{a}').strip()
        if valor.isnumeric() == True:
            num= valor
            return num
        else:
            print('\033[31mERRO! O dado inserido não pertece à classe numérica\033[m')

#Programa Principal
a = leiaInt('Digite um número: ')
print(f'O valor numérico digitado foi {a}.')
