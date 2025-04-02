from EX_97 import escreva
from time import sleep
print('\033[7;31;40m', end='')
escreva('SYSTEM OF HELP')
print('\033[7;31;40m\033[m', end='')
res = input('Função ou Biblioteca > ')
while True:
    print('\033[7;34;40m', end='')
    escreva(f'Acessando o manual de > " {res} "')
    print('\033[7;34;40m\033[m', end='')
    sleep(0.7)
    print('\033[7;30;45m', end='')
    help(res)
    print('\033[7;30;45m\033[m', end='')
    res = input('Função ou Biblioteca > ')
    if res.lower() == 'fim':
        break
    else:
        pass
