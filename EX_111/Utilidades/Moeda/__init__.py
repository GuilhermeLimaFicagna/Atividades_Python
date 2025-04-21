def fort(n):
    """
    Formatação
    """
    str(n)
    print(f'R${n:.2f}')


def moeda(n):
    print('--'*10)
    print('  Analisando valor')
    print('--'*10)
    print(f'Preço sendo analisado:  R${n:.2f}')
    print(f'O dobro é:  R${n*2:.2f}')
    print(f'A metade é:  R${n/2:.2f}')
    print(f'Aumento de 80% :  R${ n + (0.80 * n):.2f}')
    print(f'Desconto de 35% :  R${ n - (0.35 * n):.2f}')
