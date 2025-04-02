tn = int(input('Digite o termo que você deseja para saber os números da "sequência de Fibonacci: '))
n1 = 0
n2 = 1
i = 1
while i <= tn:
    tg = n1 + n2
    print('{}'.format(tg), end=' ☛ ',)
    n1 = n2
    n2 = tg
    i += 1




