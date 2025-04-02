pdp = float(input('Digite o preço do produto a ser pago:  '))
print('-=-' * 12)
fp = input('Qual a forma de pagamento:\nA vista no dinheiro ou cheque: DIGITE 1\nA vista no cartão: DIGITE 2\n2x no car'
           'tão: DIGITE 3\n3x ou mais no cartão: DIGITE 4\nInsira a forma de pagamento:  ')
print('-=-' * 12)
if fp == '1':
    print('Como você pagou a vista com dinheiro, você teve um desconto de 10%')
    dct = pdp - (pdp * 0.1)
    print('O valor do seu produto tera um desconto de {:.2f} ficando com o valor de {:.2f} R$'.format(pdp * 0.1, dct))
elif fp == '2':
    print('Como você pagou a vista no cartão, você teve um desconto de 5%')
    dct = pdp - (pdp * 00.5)
    print('O valor do seu produto tera um desconto de {:.2f} ficando com o valor de {:.2f} R$'.format(pdp * 00.5, dct))
elif fp == '3':
    print('Como você pagou em duas vezes no cartão, você não teve nem um desconto')
    print('O valor do seu produto é {:.2f} R$'.format(pdp))
else:
    print('Como você pagou em 3 ou mais vezes no cartão, você tera que pagar um juros de 20%')
    js = pdp + (pdp * 0.2)
    print('O valor do seu produto tera juros de {:.2f} ficando com o valor de {:.2f} R$'.format(pdp * 0.2, js))










