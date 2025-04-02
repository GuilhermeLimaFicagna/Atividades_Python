from random import choice
print('Jogo de pedra, papel ou tesoura')
print('-==-' * 16)
myop = input('Escolha pedra, papel ou tesoura para ver se você ganha de mim:  ')
print('-==-' * 16)
list = ['Pedra', 'Papel', 'Tesoura']
alt = choice(list)
if alt == 'Pedra':
    if myop.upper() == 'PEDRA':
        print('vish deu empate ksks {} com {} da empate'.format(myop, alt))
    elif myop.upper() == 'PAPEL':
        print('Ganhou ksks {} com {} da vitória'.format(myop, alt))
    else:
        print('perdeu trouxa skksks {} com {} da derrota'.format(myop, alt))
if alt == 'Papel':
    if myop.upper() == 'PAPEL':
        print('vish deu empate ksks {} com {} da empate'.format(myop, alt))
    elif myop.upper() == 'TESOURA':
        print('Ganhou ksks {} com {} da vitória'.format(myop, alt))
    else:
        print('perdeu trouxa skksks {} com {} da derrota'.format(myop, alt))
if alt == 'Tesoura':
    if myop.upper() == 'TESOURA':
        print('vish deu empate ksks {} com {} da empate'.format(myop, alt))
    elif myop.upper() == 'PEDRA':
        print('Ganhou ksks {} com {} da vitória'.format(myop, alt))
    else:
        print('perdeu trouxa skksks {} com {} da derrota'.format(myop, alt))
