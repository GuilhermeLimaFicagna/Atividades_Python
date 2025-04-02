listanota = list()
listanome = list()
while True:
    nm = list()
    nm.append(input('Nome: '))
    listanome.append(nm[:])

    notas = list()
    notas.append(float(input('primeira nota: ')))
    notas.append(float(input('segunda nota: ')))
    listanota.append(notas[:])

    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break

print('-='*10, 'Boletim', '-='*10)
print('No. NOMES        MÉDIAS')
for i in range(len(listanome)):
    md = (sum(listanota[i]))/2
    print('{}   {}         {}'.format(i, listanome[i][:], md))

while True:
    notas = int(input('Deseja ver nota de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    else:
        print('As notas de {} são {}'.format(listanome[notas], listanota[notas]))
