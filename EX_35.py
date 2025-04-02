print('Digite o valor de três retas..\nPara saber se com elas é ou não possível formar um triangulo:')
n1 = int(input('Primeiro comprimento de reta: '))
n2 = int(input('Segundo comprimento de reta:  '))
n3 = int(input('Terceiro comprimento de reta:  '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com essas retas, é possível sim fazermos um triangulo')
else:
    print('Com essas retas, não é possível fazermos um triangulo')
