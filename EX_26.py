n1 = input('digite uma frase de no minemo 3 palavras:  ').strip()
n2 = (n1.upper()).count('A')
n3 = (n1.upper()).find('A')+1
n4 = (n1.upper()).rfind('A')+1
print('Pelo que analisamos da sua fraze..')
print('A letra "A" aparece: {}'.format(n2))
print('A letra "A" aparece a partir da {}° posição'.format(n3))
print('A ultima vez que a letra "A" aparece e a partir da posição: {} '.format(n4))
