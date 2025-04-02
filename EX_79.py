nums = []
while True:
    nm = int(input('Digite um número, qualquer: '))
    nums.append(nm)
    res = input('Deseja continuar? [s/n]: ')[0].lower()
    if 's' in res:
        pass
    else:
        break
nums.sort()
print('voce fez essa lista de valores: {}'.format(nums))
