print('Digite seu peso e sua altura para calcularmos seu IMC.')
ps = float(input('Peso:  '))
al = float(input('Altura:  '))
IMC = ps / (al * al)
IMC = round(IMC, 0)
if IMC < 18.5:
    print('Você esta abaixo do peso.')
elif IMC in list(range(19, 25)) and 18.6 and 18.7 and 18.8 and 18.9:
    print('Você esta no peso ideal.')
elif IMC in list(range(25, 30)):
    print('Você esta com sobrepeso.')
elif IMC in list(range(30, 40)):
    print('Você esta obeso.')
else:
    print('Você esta com obesidade mórbida.')
