print('A seguir, todos os números de 1 a 50 que são pares (Vão estar em vermelho):')
print('Dos números', list(range(1, 51)), 'so esses são \033[91m pares\033[m')
for i in range(1, 51, 2):
    print('\033[91m', i + 1, '\033[m')
