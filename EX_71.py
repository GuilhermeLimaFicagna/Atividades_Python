print('-='*8)
print('Simulador de caixa eletrônico')
print('-='*8)
vl = int(input('Digite o valor a ser sacado: '))
tt = vl
ced = 50
ttced = 0
while True:
    if tt >= ced:
        tt -= ced
        ttced += 1
    else:
        if ttced > 0:
            print('Receba {} notas de {}'.format(ttced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 20:
            ced = 1
        ttced = 0
        if tt == 0:
            break
print('Até a proxima')
