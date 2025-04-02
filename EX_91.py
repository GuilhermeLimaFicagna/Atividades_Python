from random import randint
from time import sleep
resultado = {'jogador1': '', 'jogador2': '', 'jogador3': '', 'jogador4': '', }
for j in resultado.keys():
    cont = 1
    resultado[j] = int(randint(1, 6))
for k, v in resultado.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

print('Ranking dos jogadores:')

ordem = dict(sorted(resultado.items(), key=lambda itens: itens[1], reverse=True))
cont = 1
for k, v in ordem.items():
    print(f'{cont}° lugar: {k} com {v}')
    sleep(0.5)
    cont += 1
