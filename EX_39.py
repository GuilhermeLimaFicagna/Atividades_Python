nm = input('Informe seu nome:  ')
dt = int(input('Informe o seu ano de nascimento:  '))
dt = 2024 - dt
if dt < 18:
    print('Você ainda vai se alistar ao serviço militar. E vão faltar {} anos para se alistar'.format(18 - dt))
elif dt == 18:
    print('Meu fi.. ta na hora ja ksksk')
else:
    print('Ta veio em amigo pode ficar de boa')

