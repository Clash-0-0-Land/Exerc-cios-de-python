import datetime
ano = datetime.date.today().year
dados = {}
dados['nome'] = str(input('Nome: '))
year= int(input('Ano de nascimento: '))
dados['idade'] = ano-year
dados['ctps']= int(input('Número da Carteira de Trabalho (0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - ano)
print('='*30)
for k, v in dados.items():
    print(f'    -- {k} tem o valor {v}.')