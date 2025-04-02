def area(b, h):
    a = b * h
    print(f'A areá do seu terreno {b} * {h} é igual a : {a}m²')


base = float(input('Digite a base do seu terreno: '))
altura = float(input('Digite a altura do seu terreno: '))

area(base, altura)
