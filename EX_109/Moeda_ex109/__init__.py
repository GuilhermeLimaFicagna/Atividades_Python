def dobro(n, show=True):
    dou = n * 2
    if show != False:
        return str(f'R${dou:.2f}')
    else:
        return dou


def metade(n, show=True):
    div = n / 2
    if show != False:
        return str(f'R${div:.2f}')
    else:
        return div


def moeda(n, show=True):
    """
    Formatação
    """
    if show != False:
        return str(f'R${n:.2f}')
    else:
        return n

