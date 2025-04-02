nums = []
for i in range(0, 5):
    vlr = int(input('digite 5 valores:'))
    nums.append(vlr)
print('O menor valor digitado foi {},e sua posição é a {}º'.format(min(nums), nums.index(min(nums))+1))
print('O maior valor digitado foi {},e sua posição é a {}º'.format(max(nums), nums.index(max(nums))+1))
