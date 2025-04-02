lista = []
print('Digite 5 números')
for i in range(0, 5):
    n1 = int(input(f'{i+1}º número: '))
    if i == 0:
        print('Número adicionado ao começo da lista')
        lista.append(n1)
    elif n1 > lista[-1]:
        print('Número adicionado ao final da lista')
        lista.append(n1)
    else:
        print('Número adicionado ao meio da lista')
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                break
            pos += 1
print(lista)

