palavras = ('banana', 'computador', 'girafa', 'abacaxi', 'chocolate', 'elefante', 'pipoca', 'flor', 'avião', 'sorvete')
for p in palavras:
    print('\nas vogais da palavra \033[0;31m{}\033[m são: '.format(p.upper()),end='')
    for lt in p:
        if lt.lower() in 'aeiou':
            print(f'{lt} ', end='')
