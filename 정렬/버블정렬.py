# 01. 데이터가 두개 일때 버블정렬하기
data_list = [10,2]

def bubblesort(data):
  
  for index in range(len(data) - 1):
    is_change = False
    for index2 in range(len(data) - index - 1):
      if data[index2] > data[index2 + 1]:
        data[index2],data[index2 + 1] = data[index2 + 1],data[index2]
        is_change = True
    
    if is_change == False:
      break   
  return data  
    
# 체크 해보기
import random
data_list = random.sample(range(100),50)
print(bubblesort(data_list))