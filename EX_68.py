from random import choice
print('-=' * 9)
print('JOGO PAR OU IMPAR')
print('-=' * 9)
maquinanum = 0
minhaescolha = 0
tent = 0
while True:
    maquinanum = choice([1, 2])
    minhaescolha = int(input('Escolha um número: '))
    ip = input('Impar ou Par ?: ').lower()[0]
    if ip == 'i':
        if (minhaescolha + maquinanum) % 2 != 0:
            print('Você venceu, boa hehe')
            tent += 1
        else:
            print('Puts... Perdeu ksksks\nSeu número de vitorias foi de {}'.format(tent))
            break
    if ip == 'p':
        if (minhaescolha + maquinanum) % 2 != 1:
            print('Você venceu, boa hehe')
            tent += 1
        else:
            print('Puts... Perdeu ksksks\nSeu número de vitorias foi de {}'.format(tent))
            break
