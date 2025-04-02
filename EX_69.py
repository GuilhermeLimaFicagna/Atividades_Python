print('===== CADASTRO DE PESSOAS =====')
sx = ''
cid = 0
h = 0
m20 = 0
while True:
    while sx != 'f' and sx != 'm':
        sx = input('Sexo [m/f]: ')[0].lower()
    id = int(input('Idade: '))
    res = input('Quer continuar com o cadastro [s/n]: ')[0].lower()
    if sx == 'm':
        h += 1
    if id > 18:
        cid += 1
    if sx == 'f' and id < 20:
        m20 += 1
    sx = ''
    if res == 's':
        pass
    else:
        break

print('===== CADASTRO DE PESSOAS =====')
print('Concluímos que\nO número de pessoas com mais de 18 ANOS é de : {} pessoas.'.format(cid))
print('O número de homens cadastrados foi de : {} pessoas.'.format(h))
print('O número de mulheres com menos de 20 ANOS é de: {}'.format(m20))
