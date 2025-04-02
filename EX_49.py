n1 = int(input('Escolha um numero\npara exibir sua tabuada:  '))
print('A tabuada do {} é:  '.format(n1))
for i in range(1, 11):
    print('-*-' * 4)
    print('{} x {} é igual a: {}'.format(i, n1, i*n1))