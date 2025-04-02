def sortear():
    import random, time
    l = list()
    for i in range(0, 5):
        l.append(random.randint(0, 10))

    print(f'Os números sorteados foram: ', end='')
    for c in l:
        print(f'{c} ', end='')
        time.sleep(0.2)
    return l


def somai(lista):
    sum = 0
    for i in lista:
        if i % 2 == 0:
            sum += i
        else:
            pass
    print(f'A soma deles é igual a: {sum}')


a = sortear()
print('\n', '-=' * 10)
somai(a)
