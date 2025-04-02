print('Digite o valor de três retas..\nPara saber se com elas é ou não possível formar um triangulo:')
n1 = int(input('Primeiro comprimento de reta: '))
n2 = int(input('Segundo comprimento de reta:  '))
n3 = int(input('Terceiro comprimento de reta:  '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com essas retas, é possível sim fazermos um triangulo')
    if n1 == n2 and n2 == n3 and n3 == n1:
        print('E também sabemos que esse triangulo é Equilátero')
    elif (n1 + n2) / 2 == n1 or (n2 + n3) / 2 == n2 or (n3 + n1) / 2 == n3:
        print('E também sabemos que esse triangulo é Isósceles')
    else:
        print('E também sabemos que esse triangulo é Escaleno')
else:
    print('Com essas retas, não é possível fazermos um triangulo')
