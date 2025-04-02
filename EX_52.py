n1 = int(input('Digite qualquer número inteiro, e descubra se ele é primo ou não: '))
print('')
total = 0
for i in range(1, n1+1):
    if n1 % i == 0:
        print('\033[1;31m', end=' ')
        total += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\033[m')
if total != 2:
    print('Como o número {} teve {} divisões, ele não é um número primo'.format(n1, total))
elif total == 1:
    print('Como o número {} so tem uma divisão, ele não é primo'.format(n1))
else:
    print('Como o número {} teve {} divisões, ele é um número primo'.format(n1, total))
