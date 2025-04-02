cont = 0
sm = 0
print('Digite 999 para parar.')
while True:
    num = int(input('Digite variados números para saber a soma entre eles: '))
    if num == 999:
        break
    cont += 1
    sm += num
print(f'Você digitou {cont} e a soma entre eles é de {sm}')
