aluno = dict()
aluno['nome'] = input('nome: ')
aluno['media'] = int(input('média: '))
print(f'o nome é {aluno["nome"]} e a média é {aluno["media"]}')
if aluno['media'] < 50:
    print('reprovado')
else:
    print('aprovado')
