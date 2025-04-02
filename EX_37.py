bs = (input('Escolha qual base de conversão você quer:\n- Binario\n- octal\n- Hexadecimal\nDigite qual você quer: ').
      lower())
if bs == 'binario':
    n1 = int(input('Digite o número para convertermos: '))
    print('O resultado da conversão é', bin(n1)[2:])
elif bs == 'octal':
    n1 = int(input('Digite o número para convertermos: '))
    print('O resultado da conversão é', oct(n1)[2:])
else:
    n1 = int(input('Digite o número para convertermos: '))
    print('O resultado da conversão é', hex(n1)[2:])
