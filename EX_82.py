lista = []
while True:
    nm = int(input('Digite um número, qualquer: '))
    lista.append(nm)
    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break

listap = []
listai = []

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listap.append(lista[i])
    elif lista[i] % 2 != 0:
        listai.append(lista[i])
print('Então nossa lista completa sera: ', lista)
print('Os números pares nela eram: ', listap)
print('Os números impares nela eram: ', listai)
