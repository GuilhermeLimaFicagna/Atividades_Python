import Moeda_ex107
n1 = int(input('Digite um valor qualquer: R$'))

print(f'O Dobro de {n1:.2f} é {Moeda_ex107.dobro(n1):.2f}')
print(f'A Metade de {n1:.2f} é {Moeda_ex107.metade(n1):.2f}')
print(f'O Aumento de 13% de {n1:.2f} é {Moeda_ex107.aumentar(n1):.2f}')
print(f'O Desconto de 15% de {n1:.2f} é {Moeda_ex107.diminuir(n1):.2f}')
