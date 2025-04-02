n1 = input('digite o nome de uma cidade qualquer:  ').strip()
n3 = n1.split()
n2 = 'SANTOS' in (n3[0].upper())
print('Analisamos que a palavra "Santos" no começo da fraze, {} é {}'.format(n1, n2))
