n1 = int(input('Digite aqui qual foi a velocidade maxima que vc andou com seu carro hoje:  '))
if n1 > 80:
    mult = (n1 - 80) * 7
    print('Puts.. parece que você vai ter que pagar uma multa por ter ultrapassado a velocidade de 80 km..\nO valor da '
          'multa foi de {:.2f} R$'.format(mult))
else:
    print('Nada fora do comum, parabêns ☺')

