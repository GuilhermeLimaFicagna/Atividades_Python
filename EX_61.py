print('digite o primeiro termo de uma PA, e também sua razão. para saber os dez primeiros termos')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
dc = n1
PA = 0
print('-=-=' * 4)
print('Nossa progressão ficara da seguinte forma:')
print('-=-=' * 4)
while PA != 10:
    print(' {}'.format(dc), end=' ☛', )
    dc += n2
    PA += 1
print()
print('-=-=' * 4)
