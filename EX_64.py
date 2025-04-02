i = 0
sm = 0
nm = 0
print('se quiser encerrar o programa digite [999]')
while nm != 999:
    print('_-' * 17)
    nm = int(input('Digite quantos números vir na telha:'))
    sm += nm
    i += 1
print('-_-' * 13)
print('A quantidade de números digitados foi: {}\nE a soma de todos eles é igual a: {}.'.format(i - 1, sm - 999))
