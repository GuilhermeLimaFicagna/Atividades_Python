nm = str(input('- Qual o nome do aluno  '))
print('- Insira as notas do primeiro, segundo e terceiro trimestre do aluno', nm)
n1 = int(input('- Nota do primeiro tri  '))
n2 = int(input('- Nota do segundo tri  '))
n3 = int(input('- Nota do terceiro tri  '))
m = (n1+n2+n3)/3
m = round(m, 1)
print('- A media do aluno {}, é {}  ☺'.format(nm, m))

