listan = list()
imp = list()
par = list()
print('Digite sete números: ')
for i in range(1, 8):
    nums = int(input('{}°: '.format(i)))
    if nums % 2 != 0:
        imp.append(nums)
    else:
        par.append(nums)
listan.append(par)
listan.append(imp)
print('Os números pares foram: {}'.format(listan[0]))
print('Os números impares foram: {}'.format(listan[1]))
