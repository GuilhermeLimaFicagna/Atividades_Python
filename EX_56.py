print('Insira o nome, idade e sexo de 4 pessoas.')
smid = 0
mdid = 0
maioridh = 0
nmvelho = ''
totm = 0
for p in range(1, 5):
    print('----{}° Pessoa----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    smid += idade
    sexo = str(input('Sexo(M ou F): ')).upper()
    if p == 1 and sexo in 'M':
        maioridh = idade
        nmvelho = nome
    if sexo in 'M' and idade > maioridh:
        maioridh = idade
        nmvelho = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
mdid = smid / 4
print('pelo que observamos, a média de idade desse grupo de 4 pessoas é {}'.format(mdid))
print('também temos que o homem mais velho tem {} anos e, o nome dele é {}'.format(maioridh, nmvelho))
print('E no total são {} mulheres com menos de 20 anos'.format(totm))
