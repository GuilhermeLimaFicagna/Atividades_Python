sx = ['f', 'm']
r = ''
while r not in sx:
    r = input('Informe seu sexo(M ou F): ').lower()[0]
    if r not in sx:
        print('Resposta invalida... Tente novamente')
print('Obrigado pela informação')
