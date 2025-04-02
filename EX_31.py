n1 = float(input('Digite a distancia em Km que vc quer andar de avião:  '))
if n1 <= 200:
    vl = 0.50 * n1
    print('bom o valor da sua viagem vai ser de : {:.2f} R$'.format(vl))
else:
    vl = 0.45 * n1
    print('como sua viagem é um pouco longa.. vc recebe um desconto\nLogo você ira pagar {:.2f} R$'.format(vl))
