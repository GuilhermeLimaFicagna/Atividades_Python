tupla = []
nove = 0
tri = 0
par = []
for i in range(1, 5):
    n1 = int(input('Digite quatro valores:  '))
    if n1 == 9:
        nove += 1

    if n1 == 3:
        tri = i

    if n1 % 2 == 0:
        par.append(n1)

    tupla.append(n1)

if tri == 0:
    tri = 'Ops, não houveram aparições'
#questões abaxo:
print('voê digitou os números:', end=' ')
for t in tupla:
    print(t, end=' ')
print('\no valor nove apareceu: {} vez'.format(nove))
print('O três apareceu na posição: {}º'.format(tri))
print('Os números pares foram {}'.format(tuple(par)))

