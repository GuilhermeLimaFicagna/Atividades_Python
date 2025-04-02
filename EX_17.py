from math import sqrt

# Esse foi o jeito usando conceitos matemáticos

print('Escreva aqui os valores do cateto oposto e do cateto adjacente do seu triangulo retângulo \nPara calcularmos '
      'sua hipotenusa')
co = float(input('valor do cateto oposto:  '))
ca = float(input('valor do cateto adjacente:  '))
hi = ((co ** 2)+(ca ** 2)) ** 0.5
print('O valor da hipotenusa do seu triangulo retângulo é:{:.2f}'.format(hi))

print()
# Agora o jeito usando mudulo
print()

print('Escreva aqui os valores do cateto oposto e do cateto adjacente do seu triangulo retângulo \nPara calcularmos '
      'sua hipotenusa')
co = float(input('valor do cateto oposto:  '))
ca = float(input('valor do cateto adjacente:  '))
hi = sqrt(((co ** 2)+(ca ** 2)))
print('O valor da hipotenusa do seu triangulo retângulo é:{:.2f}'.format(hi))

# na biblioteca math temos a função hypot, que também faz o cálculo da hipotenusa
