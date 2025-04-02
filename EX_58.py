from random import randint, choice
numl = randint(0, 10)
nt = 1
n1 = int(input('Tente adivinhar o numero que o computador escolher\nDigite um numero inteiro de 0 a 10:  '))
if n1 != numl:
    print('Muito ruim ksksks errou')
    nt += 1
while n1 != numl:
    n1 = int(input('Tente novamente:  '))
    if n1 != numl:
        print('Muito ruim ksksks errou')
    nt += 1
print('Parabêns man, se acerto. O número era o {}\nE seu número de tentativas foi de {}'.format(numl, nt))
