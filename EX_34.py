n1 = float(input('Digite seu salario:  '))
if n1 > float(1250.00):
    amt = (n1 * 0.10) + n1
    print('Pelo calculos que fizemos, seu aumento é de 10% logo ganhara {:.2f} ☺'.format(amt))
else:
    amt = (n1 * 0.15) + n1
    print('Pelo calculos que fizemos, seu aumento é de 15% logo ganhara:\033[4;31;42m {:.2f} ☺\033[m'.format(amt))

