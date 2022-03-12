# Node 구현
from platform import node


class Node:
  def __init__(self,data,next = None):
    self.data = data
    self.next = next
    
node1 = Node(1);
node2 = Node(2);

node1.next = node2
head = node1

print(head)

# 링크드 리스트로 데이터 추가하기
def add(data):
  node = head
  # 마지막 노드 찾기
  while node.next:
    node = node.next
  node.next = Node(data)
  
  
# 링크드 리스트로 데이터 추가하기
for index in range(3,11):
  add(index)
  
# 데이터를 출력해보기
def printData(node):
  while node.next:
    print(node.data)
    node = node.next
  print(node.data)

# 실행
printData(head)

# 중간에 데이터 삽입 해보기
def Search(value):
  search = True
  node = head
  while search:
    if node.data == value:
      search = False
    else:
      node = node.next
      
  return node

node3 = Node(1.5)

next_node = Search(1).next
Search(1).next = node3
node3.next = next_node

printData(head)