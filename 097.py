def escreva(msg):
    quantidade_carateres= int(len(msg))
    cent= len('=='*quantidade_carateres)
    print('=='*quantidade_carateres)
    print(f'{msg.center(cent)}')
    print('=='*quantidade_carateres)
escreva(str(input('Digite uma frase: ')).upper().strip())
