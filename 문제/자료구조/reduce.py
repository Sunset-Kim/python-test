from functools import reduce
print(reduce(lambda x,y: y + x, 'abcd'))
# 처음에 x = a , y = b => 'ba'
# 두번째 x = ba, y = c => 'cba'
# 세번째 x = cba, y = d => 'dcba'

print('abcd')