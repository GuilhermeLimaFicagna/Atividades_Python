n1 = int(input('digite um numero de 0 a 9999:  '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100% 10
m = n1 // 1000 % 10
print('Seus dígitos separados são\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {} '.format(u, d, c, m))

