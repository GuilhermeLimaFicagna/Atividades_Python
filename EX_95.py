# Aprimorando Ex 93

listajogador = list()
listagol = list()
jogador = dict()
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} fez: '))
    listajogador.append(list(jogador.values()))

    n1 = list()
    for g in range(0, jogador['partidas']):
        n1.append(int(input(f'Quantos gols na partida {g}: ')))
    listagol.append(n1[:])

    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break

print('cod nome         Gols          Total')
for jg in range(0, len(listajogador)):
    print(f'{jg} {listajogador[jg][0]}             {listagol[jg]}         {sum(listagol[jg])}')

while True:
    n1 = int(input('Número de qual jogador: '))
    print(f'LEVANTAMENTO DO JOGADOR {listajogador[n1][0].upper()}')
    for i in range(0, listajogador[n1][1]):
        c = 0
        print(f'No jogo {i} fez {listagol[n1-c][i]}')
        c += 1
    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break
