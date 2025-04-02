print('Para aprovarmos o empréstimo, precisamos de algumas informações.. ')
vlc = float(input('Valor da casa:  '))
vls = float(input('Seu salário:  '))
ano = int(input('Em quantos anos vai pagar:  '))
vlp = (vlc / 12) / ano
vlp = round(vlp, 2)
if vlp > (vls * 0.3):
    print('Faz o L, vamo empréstar não')
else:
    print('Seu empréstimo sera bem sucedido')
