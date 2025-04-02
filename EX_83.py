n1 = input('Digite uma expressão númerica: ')
lista = []
for simb in n1:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta :)')
else:
    print('Sua expressão está errada :(')
