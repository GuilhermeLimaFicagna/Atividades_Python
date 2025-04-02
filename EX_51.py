print('digite o primeiro termo de uma PA, e também sua razão. para saber os dez primeiros termos')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
dc = n1 + (11 - 1) * n2
print('-=-=' * 4)
print('Nossa progressão ficara da seguinte forma:')
print('-=-=' * 4)
for PA in range(n1, dc, n2):
    print(' {}'.format(PA), end=' ☛', )
print()
print('-=-=' * 4)
