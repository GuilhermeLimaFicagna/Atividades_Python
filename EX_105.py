def notas(*n, show=False):
    dados = dict()
    # total ded notas
    dados['Total'] = len(n)
    # Maior nota
    dados['Maior Nota'] = max(n)
    # Menor nota
    dados['menor Nota'] = min(n)
    # Média da turma
    dados['Média da turma'] = (sum(n)/len(n))
    if show != False:
        if dados['Média da turma'] < 7.0:
            dados['Situação'] = 'RUIM'
        elif dados['Média da turma'] >= 9.0:
            dados['Situação'] = 'BOA'
        elif dados['Média da turma'] >= 7.0:
            dados['Situação'] = 'RAZOÁVEL'
    else:
        pass
    return print(dados)


notas(10, 8, 9, 3, show=True)
