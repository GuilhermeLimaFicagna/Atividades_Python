# com import

import math
ft = int(input('Digite um número, para saber seu fatorial: '))
print('-=' * 10)
print(math.factorial(ft))

# com while

ft = int(input('Digite um número, para saber seu fatorial: ')) + 1
r = 1
while ft != 1:
    ft -= 1
    r *= ft
print('-=' * 10)
print('Fatorial igual a {}'.format(r))

# com for

ft = int(input('Digite um número, para saber seu fatorial: ')) + 1
r = 1
for i in range(1, ft):
    ft -= 1
    r *= ft
print('-=' * 10)
print('Fatorial igual a {}'.format(r))
