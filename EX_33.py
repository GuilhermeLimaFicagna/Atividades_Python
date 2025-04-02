print('Digite três números para saber qual é o maior e o menor')
n1 = int(input('Primeiro número:  '))
n2 = int(input('Segundo número:  '))
n3 = int(input('Terceiro número:  '))
mnr = n1
if n2 < n1 and n2 < n3:
    mnr = n2
if n3 < n1 and n3 < n2:
    mnr = n3
mir = n1
if n2 > n1 and n2 > n3:
    mir = n2
if n3 > n1 and n3 > n2:
    mir = n3
print('O menor número é {}\nE o maior é {}'.format(mnr, mir))
