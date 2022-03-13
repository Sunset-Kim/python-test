# 삽입정렬

# range(start,stop, step)
for index in range(10,1,-1):
  print(index)

data_list = [5,3,2,1]

def insert_sort(data):
  for index in range(len(data) - 1):
    for index2 in range(index + 1, 0, -1):
      if data[index2] < data[index2 - 1]:
        data[index2],data[index2 - 1] = data[index2 - 1], data[index2]
      else:
        break
    
        
insert_sort(data_list)