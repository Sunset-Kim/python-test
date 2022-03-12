from hashlib import new


class Node:
  def __init__(self,data,next = None,prev = None):
    self.prev = prev
    self.next = next
    self.data = data 
    
class NodeManagement:
  def __init__(self,data) :
    self.head = Node(data)
    self.tail = self.head
    
  def insert(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.head
      while node.next:
        node = node.next
      new = Node(data)
      node.next = new
      new.prev = node
      self.tail = new
      
  def insert_after(self,data, search_data):
    if self.head == None:
      self.head = Node(data)
      return True
    
    # 찾자
    node = self.head
    while node.data != search_data:
      node = node.next
      if node == None:
        return False 
    
    new_node = Node(data)
    current_node = node
    after_node = node.next
    
    # 앞 연결
    current_node.next = new_node
    new_node.prev = current_node
    # 뒤 연결
    new_node.next = after_node
    after_node.prev = new_node
    
    return True
    
    
  def insert_before(self,data, before_data):
    if self.head == None:
      self.head = Node(data)
      return True
    
    node = self.tail
    while node.data != before_data:
      node = node.prev
      if node == None:
        return False
    
    new = Node(data)
    before_new = node.prev
    before_new.next = new
    new.prev = before_new
    new.next = node
    node.prev = new
    return True
      
      
  def search_from_tail(self,data):
    if self.head == None:
      return False
  
    node = self.head
    while node.next:
      if node.data == data:
        return node
      else:
        node = node.next
    return False
    
  def search_from_tail(self,data):
    if self.head == None:
      return False
    
    node = self.tail
    while node.prev:
      if node.data == data:
        return node
      else:
        node = node.prev
    return False
  
  
  
  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

double_linked_list = NodeManagement(0)

for data in range(1,10):
  double_linked_list.insert(data)
  
double_linked_list.insert_before(1.5,2)
double_linked_list.insert_after(1.7,1.5)

double_linked_list.desc()
