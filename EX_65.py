soun = ''
num = i = nm = 0
list = []
while soun != 'N':
    print('_-' * 17)
    i += 1
    num = int(input('Digite quantos números vir na telha: '))
    nm += num
    list.append(num)
    soun = input('Ainda quer continuar [S] ou [N]: ').upper()
print(nm, i)
print('A média dos valores que você digitou é: {}\nO menor número é: {}\nO maior número é: {}'.format(nm/i,
                                                                                                      min(list), max(
                                                                                                          list)))
