fz = input('Digite uma frase qualquer, e saiba se ela é um palíndromo: ').lower()
if (''.join(fz.split())) == (''.join(fz[::-1].split())):
    print('Essa frase é considerada um palíndromo')
else:
    print('Essa frase não é considerada um palíndromo')
