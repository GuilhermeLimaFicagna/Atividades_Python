km = float(input('Quantos Km você percorreu com esse carro de aluguel:  '))
ds = int(input('Por quantos dias ele foi alugado?  '))
total = (km * 0.15) * (ds * 60)
print('o preço a ser pago pelo aluguel desse carro é:  {:.2f}R$'.format(total))
