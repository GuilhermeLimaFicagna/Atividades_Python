num = ('zer0', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = int(input('digite um número de 1 a 20: '))
while escolha not in range(1, 21):
    escolha = int(input('Tente novamente. Digite um número entre 1 a 20: '))
print('Você escolheu o número: {}'.format(num[escolha]))
