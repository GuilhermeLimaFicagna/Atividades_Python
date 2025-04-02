def contador(incio, fim, razao):
    from time import sleep
    # Caso que o contador vai do menor pro maior.
    if incio < fim:
        print(f'a contagem de {incio} até {fim} indo de {razao} em {razao}', end=' => ')
        fim += 1
        for c in range(incio, fim, razao):
            print(c, end='| ')
            sleep(0.2)
        print('\n')
    # Caso que o contador vai do maior pro menor.
    # temos 3 casos, < > ou  = a "0"
    elif incio > fim:
        if fim > 0:
            print(f'a contagem de {incio} até {fim} indo de {razao} em {razao}', end=' => ')
            fim -= 1
            razao -= (razao * 2)
            for c in range(incio, fim, razao):
                print(c, end='| ')
                sleep(0.2)
            print('\n')
        elif fim == 0:
            print(f'a contagem de {incio} até {fim} indo de {razao} em {razao}', end=' => ')
            fim = -1
            razao -= (razao * 2)
            for c in range(incio, fim, razao):
                print(c, end='| ')
                sleep(0.2)
            print('\n')
        else:
            print(f'a contagem de {incio} até {fim} indo de {razao} em {razao}', end=' => ')
            fim += -1
            razao -= (razao * 2)
            for c in range(incio, fim, razao):
                print(c, end='| ')
                sleep(0.2)
            print('\n')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora faça seu contador personalizado ')
inicio = int(input('Seu inicío: '))
fim = int(input('Seu fim: '))
razao = int(input('Seu razão: '))

contador(inicio, fim, razao)