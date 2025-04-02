from datetime import date
ano = date.today().year
tt1 = 0
tt2 = 0
print('Digite a data de nascimento de sete pessoas: ')
for i in range(1, 8):
    n1 = int(input('{}° data: '. format(i)))
    if (ano - n1) >= 18:
        tt1 += 1
    else:
        tt2 += 1
print('Pelo que analisamos... {} Pessoas não atingiram a maior idade\nE ja {} Pessoas atingiram'.format(tt2, tt1))
