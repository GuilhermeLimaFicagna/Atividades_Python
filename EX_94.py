listadc = list()
pessoa = dict()
while True:
    #cadastro nome e sexo e idade

    pessoa["nome"] = input('Nome: ')
    pessoa["sexo"] = input('sexo [F/M]: ')
    pessoa["idade"] = int(input('idade: '))
    listadc.append(list(pessoa.values()))

    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break
print(listadc)
print(f'O total de pessoas cadastradas foi de {len(listadc)}')

cont = 0
for p in range(0, len(listadc)):
    mp = listadc[p][2]
    cont += mp
mp = cont / len(listadc)
print(f'A média de idade do grupo foi de {mp:.2f}')

listam = list()
for f in range(0, len(listadc)):
    if listadc[f][1] == 'f':
        listam.append(listadc[f][0])
    else:
        pass
print(f'As mulheres são: {listam}')

listai = list()
for i in range(0, len(listadc)):
    if listadc[i][2] > mp:
        listai.append(listadc[i][0])
    else:
        pass
print(f'As pessoas com maior idade são: {listai}')
