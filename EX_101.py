def voto(year=0):
    """
    Fala se vocÇe vai votar ou não
    :param year: ano de nascimento
    :return: se você pode votar ou não
    """
    from datetime import date

    yearSystem = date.today().year
    age = yearSystem - year
    if age >= 70:
        return print(f'Voto Opcional por conta de você ter {age}')
    elif age >= 18:
        return print(f'Voto Obrigatório por conta de você ter {age}')
    else:
        return print(f'Voto Nulo por conta de você ter {age}')


res = int(input('Digite o ano de nascimento e saiba se seu voto é Nulo, Obrigatório ou Opcional: '))
voto(res)
