matrix = list()
pares = list()
print('Digite nove números para inserirmos na matrix 3x3')

xx = list()
for x in range(0, 3):
    num = (int(input('valor para [0;{}]: '.format(x))))
    xx.append(num)
    if num % 2 == 0:
        pares.append(num)
matrix.append(xx)

yy = list()
for y in range(0, 3):
    num = (int(input('valor para [0;{}]: '.format(y))))
    yy.append(num)
    if num % 2 == 0:
        pares.append(num)
matrix.append(yy)

zz = list()
for z in range(0, 3):
    num = (int(input('valor para [0;{}]: '.format(z))))
    zz.append(num)
    if num % 2 == 0:
        pares.append(num)
matrix.append(zz)

print('Teremos a seguinte Matriz')
print('\033[91m', matrix[0], '\n', matrix[1], '\n', matrix[2], ' \033[m',)

print('A soma de todos os valores digitados é igual a: \033[91m{}\033[m'.format(sum(pares)))
soma = matrix[0][2] + matrix[1][2] + matrix[2][2]
print('A soma dos valore da terceira coluna é: \033[91m{}\033[m'.format(soma))

print('O maior valor da segunda linha é: : \033[91m{}\033[m'.format(max(yy)))
