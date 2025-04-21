def leiaDinheiro(*args):
    n = str
    while n != float or int:
        n = input(*args)
        if n.upper()[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print(f'\033[0;31mERRO. "{n}" não é um valor monetário\033[m')
        else:
            n = int(n)
            return n
