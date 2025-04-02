# Faça um programa que leia algo e mostre seu tipo primitivo e tudo qualquer tipo de informação
n1 = input("digite algo para saber de que tipo primitivo ele é, e também qual quer outra informação sobre ele:   ")

print("-_-_-_"*1)

print("o tipo primitivo é?   ", type(n1))

print("-_-_-_"*2)     #so pra organizar

print("ele é um numero?   ", n1.isnumeric())

print("-_-_-_"*3)

print("ele tem espaço?   ", n1.isspace())

print("-_-_-_"*4)

print("ele é numero alfabeto?   ", n1.isalpha())

print("-_-_-_"*5)

print("ele é alfabeto e numero?   ", n1.isalnum())

print("-_-_-_"*6)

print("ele esta em maiúsculas?   ", n1.isupper() )

print("-_-_-_"*7)

print("ele esta em minúsculas?  ", n1.islower())

print("-_-_-_"*8)

print("esta com a primeira letra em maiúscula?", n1.istitle())

print("-_-_-_"*9)





