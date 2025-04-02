listagol = list()
jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} fez: '))
for g in range(0, jogador['partidas']):
    listagol.append(int(input(f'Quantos gols na partida {g}: ')))
jogador['listagol'] = listagol
jogador['totgol'] = sum(listagol)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i in range(0, len(listagol)):
    print(f'    -> Na partida {i}, fez {listagol[i]} gols.')
print(f'O total de gols foi {jogador["totgol"]}')
