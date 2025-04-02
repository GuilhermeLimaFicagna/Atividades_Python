def leiInput(n):
    if n.isdigit() == False:
        num = 0
        while num == 0:
            print('\033[0;31mERRO!!!  VOCÊ DIGITOU UMA STRING\033[m')
            n = input('Digite novamente outro número: ')
            if n.isdigit():
                num = int(n)
            else:
                pass
        print(f'Você digitou o número {num}')
    else:
        print(f'Você digitou o número {n}')


num = input('Digite um número: ')
leiInput(num)
