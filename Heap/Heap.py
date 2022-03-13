# 완전이진트리
# 차이점 - 최대 및 최소만 보장 나머지 child의 순서는 고려하지 않음

# heap은 보통 배열로 표현함
# 1. 부모 노드 인덱스 번호 = 자식노드 인덱스 번호 // 2
index = 2
print(index // 2)

# 2. 왼쪽 자식노드 인덱스 번호 = 부모노드 인덱스 번호  * 2
# 3. 오른쪽 자식노드 인덱스 번호  = 부모노드 인덱스 번호 * 2 + 1

class Heap:
  # 0번부터 하면 헷갈리니까 1번 부터 할려고 None 넣음
  def __init__(self,data):
    self.heap_array = list()
    self.heap_array.append(None)
    self.heap_array.append(data)
    
  def move_up(self,inserted_index):
    if inserted_index <= 1:
      return False
    
    parent_index = inserted_index // 2
    if self.heap_array[inserted_index] > self.heap_array[parent_index]:
      return True
    else:
      return False
    
  def move_down(self,poped_index):
    return True
    
  def insert(self,data):
    if len(self.heap_array) == 0:
      self.heap_array.append(None)
      self.heap_array.append(data)
      return True
    
    self.heap_array.append(data)
    
    inserted_index = len(self.heap_array) - 1
    
    while self.move_up(inserted_index):
      parent_index = inserted_index // 2
      self.heap_array[inserted_index], self.heap_array[parent_index] = self.heap_array[parent_index],self.heap_array[inserted_index]
      inserted_index = parent_index
  def move_down(self, root_index):
    left_child_index = root_index * 2
    right_child_index = root_index * 2 + 1
    
    # case1: 왼쪽 자식 노드도 없을 때
    if left_child_index >= len(self.heap_array):
        return False
    # case2: 오른쪽 자식 노드만 없을 때
    elif right_child_index >= len(self.heap_array):
        if self.heap_array[root_index] < self.heap_array[left_child_index]:
            return True
        else:
            return False
    # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
    else:
        if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
            if self.heap_array[root_index] < self.heap_array[left_child_index]:
                return True
            else:
                return False
        else:
            if self.heap_array[root_index] < self.heap_array[right_child_index]:
                return True
            else:
                return False
  
  def pop(self):
    if len(self.heap_array) <= 1:
      return None
    
    returned_data = self.heap_array[1]
    self.heap_array[1] = self.heap_array[-1]
    del self.heap_array[-1]
    root_index = 1
    
    while self.move_down(root_index):
      left_child_index = root_index * 2
      right_child_index = root_index * 2 +1

      # 오른쪽 자식 노드만 없을때 => 새로 넣은 root와 왼쪽 자식만 비교 => 크면 교체
      if right_child_index >= len(self.heap_array):
        if self.heap_array[root_index] < self.heap_array[left_child_index]:
          self.heap_array[root_index], self.heap_array[left_child_index] = self.heap_array[left_child_index], self.heap_array[root_index]
          root_index = left_child_index
          
      # 왼쪽 오른쪽 둘다 있을때 => 오른쪽 왼쪽의 값 비교 => 큰값과 root를 비교 => 크면 교체 => 아니면 그냥 둔다
      else:
        if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
            if self.heap_array[root_index] < self.heap_array[left_child_index]:
                self.heap_array[root_index], self.heap_array[left_child_index] = self.heap_array[left_child_index], self.heap_array[root_index]
                root_index = left_child_index
        else:
            if self.heap_array[root_index] < self.heap_array[right_child_index]:
                self.heap_array[root_index], self.heap_array[right_child_index] = self.heap_array[right_child_index], self.heap_array[root_index]
                root_index = right_child_index  
          
    return returned_data
  
heap = Heap(15)
heap.insert(13)
heap.insert(12)
heap.insert(16)
heap.insert(9)
heap.insert(18)
heap.insert(7)
heap.insert(6)

heap.pop()
heap.pop()
heap.pop()
heap.pop()

print(heap.heap_array)
