from datetime import date
ano = int(input('Digite a sua data de nascimento, para encarcharmos você em sua categoria especifica:  '))
id = date.today().year - ano
if id in list(range(1, 10)):
    print('Categoria: \033[1;31;46mMIRIM\033[m')
elif id in list(range(9, 15)):
    print('Categoria: \033[1;31;46mINFANTIL\033[m')
elif id in list(range(14, 20)):
    print('Categoria: \033[1;31;46mJUNIOR\033[m')
elif id in list(range(19, 22)):
    print('Categoria: \033[1;31;46mSÊNIOR\033[m')
else:
    print('Categoria: \033[1;31;46mMASTER\033[m')


