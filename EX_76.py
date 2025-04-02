listap = ('lapis', 3.12, 'cadeira', 500, 'borracha', 12)
for i in range(0, len(listap)):
    if i % 2 == 0:
        print('{:.<30}'.format(listap[i]), end='')
    else :
        print(' R$ {:^4.2f}'.format(listap[i]))

