lista = []
while True:
    nm = int(input('Digite um número, qualquer: '))
    lista.append(nm)
    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break
print('A quantidade números digitados foram: ', len(lista))
lista.sort(reverse=True)
print('Essa lista em ordem decrescente é : ', lista)
if 5 in lista:
    print('O número "5" esta na lista')
else:
    print('O número "5" não esta na lista')

