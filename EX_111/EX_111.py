from Utilidades import Moeda, dados
# usando o princípio de modularização
n = float(input('Digite um valor: '))
Moeda.moeda(n)
print(f'Valor formatado: {Moeda.fort(n)}')

