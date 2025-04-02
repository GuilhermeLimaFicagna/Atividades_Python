from random import randint, choice
n1 = int(input('Tente adivinhar o numero que o computador escolher\nDigite um numero inteiro de 0 a 5:  '))
lista = [randint(0, 5)]
numl = choice(lista)
if n1 == numl:
    print('Parabêns man, se acerto')
else:
    print('Muito ruim ksksks errou\nO número era ', numl)
