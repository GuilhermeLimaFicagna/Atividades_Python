n1 = int(input('Digite um ano qualquer e saiba se ele e bissexto:  '))
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('parabêns !!! o ano {} é bissexto'.format(n1))
else:
    print('O ano {} não é bissexto ksksks'.format(n1))
