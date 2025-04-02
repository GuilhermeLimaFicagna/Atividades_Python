print('-=' * 20)
print('Escolha dois números e em seguida\nEscolha o que deseja:')
print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Saír do programa')
escolha = 0
while escolha != 5:
    print('-=' * 20)
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    escolha = int(input('escolha: '))
    if escolha == 1:
        print('A soma de {} e {}, é igual a\033[91m {} \033[m'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('A multiplicação de {} e {}, é igual a\033[91m {} \033[m'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é\033[91m {} \033[m'.format(n1, n2, n1))
        elif n1 < n2:
            print('O maior número entre {} e {} é\033[91m {} \033[m'.format(n1, n2, n2))
        elif n1 == n2:
            print('Os números {} e {} são iguais'.format(n1, n2))
        else:
            break
print('\033[91mFim do programa \033[m')
