from time import sleep
print('A apresentação de fogos de artificio começa em ...')
for i in range(10, -4, -1):
    print(i)
    sleep(0.7)
for i in range(0, 9):
    print('\033[91mPOW\033[m')
    print('                                            \033[91mPOW\033[m')
    sleep(0.3)
    print('             \033[91mPOW\033[m')
print('Cabo ksks')
