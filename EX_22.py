n1 = str(input('Digite o nome do seu amigo:  '))
lma = n1.upper()
lmi = n1.lower()
lt = len(''.join(n1.split()))
lpn = len(n1.split()[0])

print('Sobre as analises que fiz sobre o nome "{}", temos que\nInteiro maiúsculo: {}\nInteiro minúsculo: {}\nTotal de'
      'letras: {}\nTotal de letras do primeiro nome: {}'.format(n1, lma, lmi, lt, lpn))
