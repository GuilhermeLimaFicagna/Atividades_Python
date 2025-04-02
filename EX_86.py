matrix = list()
print('Digite nove números para inserirmos na matrix 3x3')

xx = list()
for x in range(0, 3):
    xx.append(int(input('valor para [0;{}]: '.format(x))))
matrix.append(xx[:])

yy = list()
for y in range(0, 3):
    yy.append(int(input('valor para [1;{}]: '.format(y))))
matrix.append(yy)

zz = list()
for z in range(0, 3):
    zz.append(int(input('valor para [2;{}]: '.format(z))))
matrix.append(zz)

print('Teremos a seguinte Matriz')
print('\033[91m{}\n{}\n{}\n\033[m'.format(matrix[0], matrix[1], matrix[2]))
