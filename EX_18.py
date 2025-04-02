import math
n1 = int(input('Digite um angulo inteiro qualquer para saber o valor do seu seno,cosseno e tangente:  '))
n2 = math.radians(n1)
print('Valor do seno: {:.2f}\nValor do cosseno: {:.2f}\nValor da tangente: {:.2f}'.format(math.sin(n2), math.cos(n2), math.tan(n2)))



