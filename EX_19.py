import random

a1 = str('mariane')
a2 = str('Gui')
a3 = str('Bia')
a4 = str('Argentino')

lista = [a1, a2, a3, a4]

print('Entre os alunos {}, {}, {} e {}. O escolhido para apagar o quandro foi o/a\n{} ☺'.format(a1, a2, a3, a4,
                                                                                                random.choice(lista)))
