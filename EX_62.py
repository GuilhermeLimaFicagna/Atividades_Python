print('digite o primeiro termo de uma PA, e também sua razão. para saber os dez primeiros termos')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
dc = n1
PA = 0
termo = 10
print('-=-=' * 15)
print('Nossa progressão ficara da seguinte forma:')
print('-=-=' * 15)
while termo != 0:
    while PA != termo:
        print(' {}'.format(dc), end=' ☛', )
        dc += n2
        PA += 1
    print()
    PA = 0
    termo = int(input('você deseja saber mais termos na PA?\n[0] para encerrar programa: '))
    print('-=-=' * 15)
print('fim do programa')
