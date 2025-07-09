def leiInput(n):
    try:
        num = int(n)
    except:
        num = 0
        while num == 0:
            print('\033[0;31mERRO!!!  NÚMERO INVALIDO\033[m')
            n = input('Digite novamente outro número: ')
            if n.isdigit():
                num = int(n)
            else:
                pass
        print(f'Você digitou o número {num}')
    else:
        print(f'Você digitou o número {num}')
    finally:
        print("Volte sempre")


num = input('Digite um número: ')
leiInput(num)

