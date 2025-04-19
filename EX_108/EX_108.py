import Moeda_ex108
n1 = int(input('Digite um valor qualquer: R$'))

print(f'O dobro de {Moeda_ex108.moeda(n1)} é {Moeda_ex108.moeda(Moeda_ex108.dobro(n1))}')
print(f'A Metade de {Moeda_ex108.moeda(n1)} é {Moeda_ex108.moeda(Moeda_ex108.metade(n1))}')
