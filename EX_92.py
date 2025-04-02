from datetime import date

dados = dict()
dados['Nome'] = input('Digite seu nome: ')
dados['Idade'] = int(input('Digite o ano de nascimento: '))
dados['CTPS'] = int(input('Número da carteira de trabalho [Se não então 0]: '))
while dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano da contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Contratação'] - dados['Idade'] + 35
    dados['Idade'] = date.today().year - dados['Idade']
    for k, v in dados.items():
        print(f'O {k} tem valor {v}')
    break
