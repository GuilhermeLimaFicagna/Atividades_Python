print('digite seis números e veja soma entre os números pares:  ')
sm = 0
for i in range(1, 7):
    n1 = int(input('{}° número:  '.format(i)))
    if n1 % 2 != 1:
        sm += n1
print('A soma de todos os números pares que você digitou é igual a: {}'.format(sm))
