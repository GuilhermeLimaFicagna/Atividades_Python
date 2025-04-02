tn1 = float(input('Digite sua nota da prova um e logo em seguida a prova dois. Para saber se você esta de recuperação'
                  '...\nPROVA 01:  '))
tn2 = float(input('Prova 02:  '))
md = (tn2 + tn1) / 2
md = round(md, 1)
if md < 50.0:
    print('Infelizmente por você ter tirado nota {}, você foi reprovado'.format(md))
elif md >= 50.0 or md < 70.0:
    print('Infelizmente por você ter tirado nota {}, você ficou de recuperação'.format(md))
else:
    print('Felizmente por você ter tirado nota {}, você foi aprovado'.format(md))
