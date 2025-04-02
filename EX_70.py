print('-='*8)
print('LOJONA DOS GURI')
print('-='*8)

preco = 0
mil = 0
listnm = []
listpreco = []

while True:
    nm = input('Nome do produto: ')
    produto = int(input('Preço do produto: R$: '))
    preco += produto
    listnm.append(nm)
    listpreco.append(produto)

    if produto > 1000:
        mil += 1

    res = input('Deseja continuar [n/s]?: ')[0].lower()
    if res == 'n':
        break
    else:
        pass
print('O total da compra sera: {}'.format(preco))
print('Temos {} produtos custando mais de 1.000,00 R$'.format(mil))
print('O produto mais barato foi {}, custando {}R$.'.format(listnm[listpreco.index(min(listpreco))], min(listpreco)))
