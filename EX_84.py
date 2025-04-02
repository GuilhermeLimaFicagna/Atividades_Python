lista = list()
while True:
    nope = list()
    nope.append(input('Digite seu nome: '))
    nope.append(float(input('Digite seu peso: ')))
    lista.append(nope[:])
    nope.clear()

    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break
print('O número de pessoas cadastradas foi {}'.format(len(lista)))

menor = list()
maior = list()
for np in lista:
    if np[1] < 100:
        menor.append(np[0])
    else:
        maior.append(np[0])

if len(maior) > 0:
    print('As pessoas acima dos 100 KG são {}'.format(maior))
else:
    print('Não tem pessoas acima de 100kg')
if len(menor) > 0:
    print('As pessoas abaixo dos 100 KG são {}'.format(menor))
else:
    print('Não tem pessoas abaixo de 100kg')
