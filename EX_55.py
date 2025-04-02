print('Escreva o peso de cinco pessoas')
list1 = []
list2 = []
for i in range(1, 6):
    list1 = float(input('{}° pessoa: '.format(i)))
    list2.append(list1)
print('Das pessoas que você informou o peso\nA pessoa com \033[91mMENOR\033[m é : {} KG\nE a com \033[91mMAIOR\033[m é:' 
      '{} KG'
      .format(min(list2), max(list2)))
