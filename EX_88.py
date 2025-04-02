import random
from time import sleep
listadepalpites = list()
palpites = list()
print('Diga quantos palpites você quer dar na')
print('\033[91mMEGA SENA\033[m')

palps = int(input('Quantos palpites você deseja: '))
for p in range(0, palps):
    li = list(range(0, 60))
    for n in range(0, 6):
        jogo = random.choice(li)
        if jogo in palpites:
            pass
        else:
            palpites.append(jogo)
            if len(palpites) == 6:
                listadepalpites.append(palpites)
                palpites = []
            else:
                pass

print('SEUS JOGOS FORAM')
for i in range(0, len(listadepalpites)):
    print('\033[91m', sorted(listadepalpites[i]), '\033[m')
    sleep(0.3)
