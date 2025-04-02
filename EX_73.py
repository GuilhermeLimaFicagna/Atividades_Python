times = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',
         'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport',
         'Portuguesa', 'Atlético Paranaense', 'Vitória')
print('\033[0;31m-=\033[m'*110)

print('Os primeiros 5 colocados são: {}'.format(times[0:5]))

print('\033[0;31m-=\033[m'*110)

print('Os últimos 4 colocados são: {}'.format(times[-4:]))

print('\033[0;31m-=\033[m'*110)

print('A ordem alfabética desses times é: {}'.format(sorted(times)))

print('\033[0;31m-=\033[m'*110)

print('A Coritiba esta na posição {}º'.format(times.index('Coritiba') + 1))

print('\033[0;31m-=\033[m'*110)

