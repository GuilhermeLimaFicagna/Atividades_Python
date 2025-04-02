print('A seguir, a soma de todos os números impares múltiplos de 3:')
sm = 0
for m in range(0, 501, 3):
    if m % 2 == 1:
        sm += m
print(sm)


