from random import randint

lista = []
for i in range(0, 5):
    lt = randint(0, 10)
    lista.append(lt)

for l in lista:
    print(l, end= ' ')
print('\nO menor número: {}\nO maior número: {}'.format(min(lista), max(lista)))
