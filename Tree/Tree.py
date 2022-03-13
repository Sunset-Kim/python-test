class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    
class NodeMagager:
  def __init__(self,head):
    self.head = head
  
  def insert(self, value):
    current_node = self.head
    
    while True:
      if value < current_node.value:
        if current_node.left != None:
          current_node = current_node.left
        else:
          current_node.left = Node(value)
          break
      # 오른쪽 비교
      else:
        if current_node.right != None:
          current_node = current_node.right
        else:
          current_node.right = Node(value)
          break
  
  # 검색
  def search(self, value):
    current_node = self.head
    
    while current_node:
      print(current_node.value,value)
      
      if current_node.value == value:
        return True
      
      elif current_node.value < value:
        current_node = current_node.right
      else:
        current_node = current_node.left
        
      
    
    return False

  # 삭제 : 삭제할 노드의 자식의 조건에 따라서 삭제 케이스를 나눔
  def delete(self,value):
    # 삭제할 노드를 탐색
    searched = False
    self.current_node = self.head
    self.parent = self.head
    
    while self.current_node:
      if self.current_node.value == value:
        searched = True
        break
      elif value < self.current_node.node:
        self.parent = self.current_node
        self.current_node = self.current_node.left
      else:
        self.parent = self.current_node
        self.current_node = self.current_node.right
        
    if searched == False:
      return False
        
    # 1. leaf 노드 삭제
    if self.current_node.left == None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left= None
      else:
        self.parent.right = None
        
      del self.current_node
    
    # 2. child Node가 하나일 경우
    
    # 2.1 왼쪽이 살아있고 오른쪽이 없을경우
    if self.current_node.left != None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left = self.current_node.left
      else:
        self.parent.right = self.current_node.left
  
    # 2.2 왼쪽이 없고 오른쪽이 살아있을 경우
    elif self.current_node.left == None and self.current_node.right != None:
      if value < self.parent.value:
        self.parent.left = self.current_node.right
      else: 
        self.parent.right = self.current_node.right
    
    # 3 child Node가 2개일 경우
    # 3-1) 오른쪽 자식중 가장 작은값을 부모로 올린다 => 이것을 선택
    # 3-2) 왼쪽 지식중 가장 큰값을 부모로 올린다.
    if self.current_node.left != None and self.current_node.right != None:
      
      if value < self.parent.value:
        self.change_node = self.current_node.right
        self.change_node_parent = self.current_node.right
        
        while self.change_node.left != None:
          self.change_node_parent = self.change_node
          self.change_node = self.change_node.left
      
        # 3-1-2) 가장 작은값의 자식이 있을때 (오른쪽만 있을 수 있음 ; 왼쪽은 더 작은 자식이기 때문에)
        if self.change_node.right != None:
          self.change_node_parent.left = self.change.node.right
          
        # 3-1-1) 가장 작은값이 자식이 없을때    
        else:
          self.change_node_parent.left = None
        
        self.parent.left = self.change_node
        self.change_node.right = self.current_node.right
        self.change_node.left = self.change_node.left
        
      else:
        self.change_node = self.current_node.right
        self.change_node_parent = self.current_node.right
        
        while self.change_node.left != None:
          self.change_node_parent = self.change_node
          self.change_node = self.change_node.left
        
        if self.change_node.right != None:
          self.change_node_parent.left = self.change_node.right
        
        else:
          self.change_node_parent.left = None
          
        self.parent.right = self.change_node
        self.change_node.left = self.current_node.left
        self.change_node.right = self.current_node.right
    
    
    



head = Node(1)
BST = NodeMagager(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(2))