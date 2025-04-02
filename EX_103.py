def ficha(name='desconhecido', gols=0):
    return print(f'O jogador {name} fez {gols} gols')


name = input('Nome do jogador: ')
gols_input = input('Quantidade de gols: ').strip()
gols = int
if gols_input.isdigit():
    gols = int(gols_input)
else:
    gols = 0

ficha(name, gols)
