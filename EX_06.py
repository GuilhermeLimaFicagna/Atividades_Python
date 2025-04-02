n1 = int(input('escreva um numero para saber seu dobro \nseu triplo \ne sua raiz quadrada\n:  '))
d = n1*2
t = n1*3
r = n1 ** 0.5
r = round(r, 2)
print()
print("Os resultados são\nDobro de {} é igual a {}\nTriplo de {} é igual a {}\nRaiz quadrada de {} é igual a {}".format(n1, d, n1, t, n1, r))
print(r)