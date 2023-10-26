def ajuda():
    def escreva(msg):
        quantidade_carateres = len(msg)
        cent = len('==' * quantidade_carateres)
        p=f"""{'==' * quantidade_carateres}\n{msg.center(cent)}\n{'==' * quantidade_carateres}
"""
        return p
    while True:
        print(f"\033[30;47m {escreva('SISTEMA DE AJUDA PYHELP')} \033[m")
        ajuda= str(input('Função ou biblioteca >> ')).strip()
        if ajuda.upper() == 'FIM':
            escreva('\033[30;41mFIM! ATÉ A PRÓXIMA\033[m')
            break
        escreva(f'PROCURANDO O COMANDO "{ajuda}"')
        print(f'\033[34;42m{help(ajuda)}\033[m')
ajuda()