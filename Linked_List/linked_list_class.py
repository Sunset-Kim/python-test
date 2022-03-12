class Node:
  def __init__(self,data,next = None):
      self.data = data
      self.next = next
      
class NodeManagement:
  def __init__(self,data):
        self.head = Node(data)
      
  def add(self,data):
    if self.head == '':
      self.head = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)
      
  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next
      
  def delete(self, data):
    if self.head == '':
      print('해당 값을 가진 노드는 없습니다')
      return
    
    if self.head.data == data:
      temp = self.head
      self.head = self.head.next
      del temp
    else:
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp
          return
        else:
          node = node.next
  
  def search(self,data):
    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next
          
linkedList1 = NodeManagement(0);
for i in range(2,10):
  linkedList1.add(i)
  

linkedList1.delete(2);
linkedList1.desc();

print(linkedList1.search(3).next.data)