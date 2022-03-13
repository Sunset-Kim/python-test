# hash table 만들기
hash_table = list([0 for i in range(10)])

# hash 함수 만들기
def hash_func(key):
  return key % 5

# hash 테이블에 데이터 저장
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

# ord() : 문자의 ASCII 코드를 리턴한다
print(ord(data1[0]))

# 데이터 저장
def storage_data(data,value):
  key = ord(data[0])
  hash_address = hash_func(key)
  hash_table[hash_address] = value
  
storage_data('Andy', '01055553333')
storage_data('Dave', '0102222222')
storage_data('Trump', '0101111111')

print(hash_table)

# 데이터 읽기
def get_data(data):
  key = ord(data[0])
  hash_address = hash_func(key)
  return hash_table[hash_address]

print(get_data('Andy'))