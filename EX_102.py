def fatorial(num=1, show=False):
    fat = 1
    for f in range(num, 0, -1):
        fat *= f

    if show != False:
        for f in range(num, 0, -1):
            if f != 1:
                print(f'{f} x ', end='')
            else:
                print(f'1 = {fat}')
    else:
        print(fat)


fatorial(10, True)
